from fastapi import APIRouter

from app.graph.workflow import workflow
from app.schemas.api import (
    GenerateRequest,
    GenerateResponse,
)


router = APIRouter()


@router.post(
    "/generate",
    response_model=GenerateResponse
)
def generate_content(
    request: GenerateRequest
):

    result = workflow.invoke(
        {
            "topic": request.topic,
            "research": "",
            "ideas": None,
            "script": None,
        }
    )

    return result