from pydantic import BaseModel


class ScriptResponse(BaseModel):
    hook: str
    body: str
    ending: str
    cta: str