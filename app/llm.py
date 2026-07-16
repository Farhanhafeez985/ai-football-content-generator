from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
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

    elif settings.LLM_PROVIDER == "openai":
        return ChatOpenAI(
            model=settings.OPENAI_MODEL,
            api_key=settings.OPENAI_API_KEY,
            temperature=0.7,
        )

    elif settings.LLM_PROVIDER == "grok":
        return ChatGroq(
            model_name=settings.GROK_MODEL,
            temperature=0.1,
            max_tokens=1000,
        )


    elif settings.LLM_PROVIDER == "gemini":
        return ChatGoogleGenerativeAI(
            model=settings.GEMINI_MODEL,
            google_api_key=settings.GEMINI_API_KEY,
            temperature=0.7,
        )

    raise ValueError(f"Unsupported LLM Provider: {settings.LLM_PROVIDER}")