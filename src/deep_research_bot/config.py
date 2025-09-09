from dotenv import load_dotenv
import os

load_dotenv()


class Settings:
    llm: str = os.getenv("LLM", "meta-llama/Llama-4-Scout-17B-16E-Instruct")
    api_key: str = os.getenv("OPENAI_API_KEY", "")
    base_url: str = os.getenv("BASE_URL", "https://api.together.xyz/v1")
    model_family: str = os.getenv("MODEL_FAMILY", "llama_4_scout")


settings = Settings()
