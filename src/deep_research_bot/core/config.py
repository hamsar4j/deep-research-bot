from dotenv import load_dotenv
import os

load_dotenv()


class Settings:
    llm: str = os.getenv("LLM", "gpt-5-mini-2025-08-07")
    api_key: str = os.getenv("OPENAI_API_KEY", "")
    search_provider: str = os.getenv("SEARCH_PROVIDER", "tavily")
    tavily_api_key: str | None = os.getenv("TAVILY_API_KEY") or None


settings = Settings()
