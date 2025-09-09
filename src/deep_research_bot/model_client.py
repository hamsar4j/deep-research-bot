from deep_research_bot.config import settings
from dotenv import load_dotenv
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_core.models import ModelFamily

load_dotenv()

try:
    family = getattr(ModelFamily, settings.model_family)
except AttributeError:
    raise ValueError(
        f"Invalid model_family: {settings.model_family}. Must be a valid ModelFamily enum name."
    )

client = OpenAIChatCompletionClient(
    model=settings.llm,
    api_key=settings.api_key,
    base_url=settings.base_url,
    model_info={
        "vision": True,
        "function_calling": True,
        "json_output": True,
        "family": family,
        "structured_output": True,
    },
)
