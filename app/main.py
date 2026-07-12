from fastapi import FastAPI, Request

from app.config import settings
from app.llm import get_llm
# from app.agents.research import ResearchAgent
# from app.agents.topic import TopicAgent
# from app.agents.script import ScriptAgent
from app.graph.workflow import workflow
from app.api.auth import token_required
app = FastAPI(
    title="AI Football Content Generator",
    version="1.0.0"
)

@app.get("/")
def root():
    llm = get_llm()
    return {
        "message": "AI Football Content Generator API is running.",
        "provider": settings.LLM_PROVIDER,
        "model": llm.model,
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }



# @app.get("/research")
# def research(topic: str):
#     agent = ResearchAgent()
#
#     result = agent.run(topic)
#
#     return {
#         "topic": topic,
#         "research": result
#     }
#
# @app.get("/topic")
# def generate_topics(topic: str):
#     research = ResearchAgent().run(topic)
#     ideas = TopicAgent().run(research)
#     return {
#         "topic": topic,
#         "ideas": ideas,
#     }
#
# @app.get("/generate")
# def generate(topic: str):
#     research = ResearchAgent().run(topic)
#     print(research)
#     ideas = TopicAgent().run(research)
#     print(ideas)
#     script = ScriptAgent().run(ideas)
#
#     return {
#         "research": research,
#         "ideas": ideas,
#         "script": script,
#     }


@app.post("/generate")
@token_required
async def generate(request: Request):

    body = await request.json()

    topic = body.get("topic")

    result = workflow.invoke(
        {
            "topic": topic,
            "research": "",
            "ideas": None,
            "script": None,
        }
    )

    return result
