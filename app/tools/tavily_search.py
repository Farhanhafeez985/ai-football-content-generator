from langchain.tools import tool
from tavily import TavilyClient

from app.config import settings

client = TavilyClient(api_key=settings.TAVILY_API_KEY)


@tool
def tavily_search(query: str) -> str:
    """
    Search the web for the latest football information.
    """

    response = client.search(
        query=query,
        search_depth="advanced",
        max_results=5,
    )

    results = []

    for item in response.get("results", []):
        results.append(
            f"""
                Title: {item["title"]}
                
                Content:
                {item["content"]}
                """
        )

    return "\n\n".join(results)