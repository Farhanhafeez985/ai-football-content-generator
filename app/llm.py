from langchain_ollama import ChatOllama

from app.config import settings


def get_llm():
    """
    Returns the configured LLM instance.
    """

    if settings.LLM_PROVIDER == "ollama":
        return ChatOllama(
            model=settings.OLLAMA_MODEL,
            base_url=settings.OLLAMA_BASE_URL,
            temperature=0.7,
        )

    raise ValueError(f"Unsupported LLM Provider: {settings.LLM_PROVIDER}")