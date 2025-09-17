from autogen_agentchat.agents import AssistantAgent
from deep_research_bot.llm.model_client import client
from deep_research_bot.models import ClarifierResponse
from deep_research_bot.prompts import CLARIFIER_PROMPT


clarifier_agent = AssistantAgent(
    name="clarifier_agent",
    model_client=client,
    system_message=CLARIFIER_PROMPT,
    output_content_type=ClarifierResponse,
    reflect_on_tool_use=True,
    model_client_stream=True,  # Enable streaming tokens from the model client.
)
