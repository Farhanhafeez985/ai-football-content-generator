from pydantic import BaseModel

from app.schemas.topic import TopicResponse
from app.schemas.script import ScriptResponse


class GenerateRequest(BaseModel):
    topic: str


class GenerateResponse(BaseModel):
    topic: str
    research: str
    ideas: TopicResponse
    script: ScriptResponse