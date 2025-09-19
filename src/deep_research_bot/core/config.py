from dotenv import load_dotenv
import os

load_dotenv()


class Settings:
    llm: str = os.getenv("LLM", "deepseek-ai/DeepSeek-R1")
    api_key: str = os.getenv("OPENAI_API_KEY", "")
    base_url: str = os.getenv("BASE_URL", "https://api.together.xyz/v1")
    model_family: str = os.getenv("MODEL_FAMILY", "R1")
    search_provider: str = os.getenv("SEARCH_PROVIDER", "tavily")
    tavily_api_key: str | None = os.getenv("TAVILY_API_KEY") or None


settings = Settings()
