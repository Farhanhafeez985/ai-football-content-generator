from pydantic import BaseModel


class EvaluationResult(BaseModel):
    quality: str
    feedback: str