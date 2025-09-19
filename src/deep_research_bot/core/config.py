from dotenv import load_dotenv
import os

load_dotenv()


class Settings:
    llm: str = os.getenv("LLM", "meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8")
    api_key: str = os.getenv("OPENAI_API_KEY", "")
    base_url: str = os.getenv("BASE_URL", "https://api.together.xyz/v1")
    model_family: str = os.getenv("MODEL_FAMILY", "LLAMA_4_MAVERICK")
    search_provider: str = os.getenv("SEARCH_PROVIDER", "tavily")
    tavily_api_key: str | None = os.getenv("TAVILY_API_KEY") or None


settings = Settings()
