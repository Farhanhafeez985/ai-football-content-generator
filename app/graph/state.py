from typing import TypedDict


class GraphState(TypedDict):

    topic: str
    research: str
    ideas: object
    script: object
    evaluation: object
    next_agent: str
    retry_count: int
    audio_path: str
    narration: str