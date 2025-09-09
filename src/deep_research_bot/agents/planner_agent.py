from autogen_agentchat.agents import AssistantAgent
from deep_research_bot.model_client import client
from deep_research_bot.prompts import PLANNER_PROMPT
from deep_research_bot.models import WebSearchPlan


planner_agent = AssistantAgent(
    name="planner_agent",
    model_client=client,
    system_message=PLANNER_PROMPT,
    # output_content_type=WebSearchPlan,
    reflect_on_tool_use=True,
    model_client_stream=True,  # Enable streaming tokens from the model client.
)
