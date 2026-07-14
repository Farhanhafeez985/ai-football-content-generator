from .tavily_search import tavily_search
from .deepgram_tts import deepgram_tts

TOOLS = [
    tavily_search,
    deepgram_tts,
]