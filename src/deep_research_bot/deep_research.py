from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.messages import StructuredMessage
from autogen_agentchat.agents import UserProxyAgent
from autogen_agentchat.conditions import MaxMessageTermination, TextMentionTermination
from autogen_agentchat.ui import Console
from deep_research_bot.models import (
    WebSearchPlan,
    ReportData,
    ReviewFeedback,
    ClarifierResponse,
)
from deep_research_bot.agents import (
    clarifier_agent,
    planner_agent,
    search_agent,
    writer_agent,
    review_agent,
)
from deep_research_bot.model_client import client


max_msg_termination = MaxMessageTermination(max_messages=24)
review_approval_termination = TextMentionTermination("__APPROVE__")
main_termination = max_msg_termination | review_approval_termination

# Separate termination for the clarification phase (user approval)
clarify_max_msg_termination = MaxMessageTermination(max_messages=8)
# Only terminate when agent says __FALSE__ for "need_clarification"
clarify_token_termination = TextMentionTermination("__FALSE__")
clarify_termination = clarify_max_msg_termination | clarify_token_termination

user_proxy_agent = UserProxyAgent(name="user", input_func=input)


async def run_clarification(initial_task: str) -> str:
    clarification_team = RoundRobinGroupChat(
        [clarifier_agent, user_proxy_agent],
        termination_condition=clarify_termination,
        custom_message_types=[
            StructuredMessage[ClarifierResponse],
        ],
    )

    clarification_result = await Console(
        clarification_team.run_stream(task=initial_task),
        output_stats=False,
    )

    clarified_task = initial_task
    messages = list(getattr(clarification_result, "messages", []) or [])
    # Walk messages in reverse so we grab the most recent structured response from the clarifier.
    for message in reversed(messages):
        if isinstance(message, StructuredMessage) and isinstance(
            message.content, ClarifierResponse
        ):
            clarified_task = message.content.clarified_task
            break

    return clarified_task


async def run_research(task: str) -> None:
    # Phase 1: Clarify the task in a dedicated team so it terminates once well-structured.
    clarified_task = await run_clarification(task)

    # Phase 2: Use the clarified task with the main team (planner/search/writer/review).
    team = RoundRobinGroupChat(
        [planner_agent, search_agent, writer_agent, review_agent],
        termination_condition=main_termination,
        custom_message_types=[
            StructuredMessage[WebSearchPlan],
            StructuredMessage[ReportData],
            StructuredMessage[ReviewFeedback],
        ],
    )
    await Console(
        team.run_stream(task=clarified_task),
        output_stats=True,
    )
    # Close the connection to the model client.
    await client.close()
