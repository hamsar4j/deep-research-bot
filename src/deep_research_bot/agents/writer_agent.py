from autogen_agentchat.agents import AssistantAgent
from deep_research_bot.model_client import client
from deep_research_bot.prompts import WRITER_PROMPT
from deep_research_bot.models import ReportData


writer_agent = AssistantAgent(
    name="writer_agent",
    model_client=client,
    system_message=WRITER_PROMPT,
    # output_content_type=ReportData,
    reflect_on_tool_use=True,
    model_client_stream=True,  # Enable streaming tokens from the model client.
)
