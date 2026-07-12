from typing import TypedDict

from app.schemas.topic import TopicResponse
from app.schemas.script import ScriptResponse


class GraphState(TypedDict):

    topic: str
    research: str
    ideas: object
    script: object
    evaluation: object
    next_agent: str