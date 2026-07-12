from dotenv import load_dotenv
import os

load_dotenv()


class Settings:
    LLM_PROVIDER = os.getenv("LLM_PROVIDER", "ollama")

    OLLAMA_BASE_URL = os.getenv(
        "OLLAMA_BASE_URL",
        "http://localhost:11434"
    )

    OLLAMA_MODEL = os.getenv(
        "OLLAMA_MODEL",
        "qwen3:8b"
    )

    TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

    API_TOKEN = os.getenv("API_TOKEN")
    
settings = Settings()