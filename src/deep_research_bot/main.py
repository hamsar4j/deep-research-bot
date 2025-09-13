import argparse
import asyncio
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.messages import StructuredMessage
from autogen_agentchat.conditions import MaxMessageTermination, TextMentionTermination
from autogen_agentchat.ui import Console
from deep_research_bot.models import WebSearchPlan, ReportData, ReviewFeedback
from deep_research_bot.agents import (
    planner_agent,
    search_agent,
    writer_agent,
    review_agent,
)
from deep_research_bot.model_client import client


def parse_args():
    parser = argparse.ArgumentParser(description="Deep Research Bot")
    parser.add_argument("task", nargs="*", help="The research task to investigate")
    return parser.parse_args()


max_msg_termination = MaxMessageTermination(max_messages=24)
text_termination = TextMentionTermination("__APPROVE__")
combined_termination = max_msg_termination | text_termination


async def run_research(task: str) -> None:
    # Register structured message specializations so the group chat's MessageFactory knows them.
    team = RoundRobinGroupChat(
        [planner_agent, search_agent, writer_agent, review_agent],
        # max_turns=6,
        termination_condition=combined_termination,
        custom_message_types=[
            StructuredMessage[WebSearchPlan],
            StructuredMessage[ReportData],
            StructuredMessage[ReviewFeedback],
        ],
    )
    await Console(
        team.run_stream(task=task),
        output_stats=True,
    )
    # Close the connection to the model client.
    await client.close()


def main() -> None:
    args = parse_args()
    if not args.task:
        print("Error: Please provide a research task.")
        print("Usage: deep-research-bot 'Your research query here'")
        return

    task = " ".join(args.task)
    asyncio.run(run_research(task))


if __name__ == "__main__":
    main()
