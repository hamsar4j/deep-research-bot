from deep_research_bot.config import settings
from dotenv import load_dotenv
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_core.models import ModelFamily

load_dotenv()

client = OpenAIChatCompletionClient(
    model=settings.llm,
    api_key=settings.api_key,
    base_url=settings.base_url,
    model_info={
        "vision": True,
        "function_calling": True,
        "json_output": True,
        "family": ModelFamily.LLAMA_4_SCOUT,
        "structured_output": True,
    },
)
