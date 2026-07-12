from pydantic import BaseModel


class TopicIdea(BaseModel):
    title: str


class TopicResponse(BaseModel):
    ideas: list[TopicIdea]