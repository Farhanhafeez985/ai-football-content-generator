from pydantic import BaseModel


class SupervisorDecision(BaseModel):
    next_agent: str