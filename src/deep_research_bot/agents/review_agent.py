from autogen_agentchat.agents import AssistantAgent
from deep_research_bot.model_client import client
from deep_research_bot.prompts import REVIEWER_PROMPT
from deep_research_bot.models import ReviewFeedback


review_agent = AssistantAgent(
    name="review_agent",
    model_client=client,
    system_message=REVIEWER_PROMPT,
    output_content_type=ReviewFeedback,
    reflect_on_tool_use=True,
    model_client_stream=True,  # Enable streaming tokens from the model client.
)
