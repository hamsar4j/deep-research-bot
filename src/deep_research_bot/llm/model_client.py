from deep_research_bot.core.config import settings
from autogen_ext.models.openai import OpenAIChatCompletionClient

client = OpenAIChatCompletionClient(
    model=settings.llm,
    api_key=settings.api_key,
)
