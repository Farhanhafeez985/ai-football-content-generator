from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse
import json
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



# @app.post("/generate")
# @token_required
# async def generate(request: Request):
#
#     body = await request.json()
#
#     topic = body.get("topic")
#     # print(workflow.get_graph().draw_mermaid())
#     result = workflow.invoke(
#         {
#             "topic": topic,
#             "research": "",
#             "ideas": None,
#             "script": None,
#             "evaluation": None,
#             "retry_count": 0,
#         }
#     )
#     return {
#         "topic": result["topic"],
#         "research": result["research"],
#         "ideas": result["ideas"].ideas,
#         "script": result["script"],
#         "evaluation": result["evaluation"]
#     }


@app.post("/generate")
@token_required
async def generate(request: Request):

    NODE_STATUS = {
        "research": "🔍 Research Complete",
        "topic": "💡 Ideas Generated",
        "script": "✍️ Script Generated",
        "evaluator": "🧐 Script Evaluated",
    }

    body = await request.json()
    topic = body.get("topic")

    initial_state = {
        "topic": topic,
        "research": "",
        "ideas": None,
        "script": None,
        "evaluation": None,
        "retry_count": 0,
    }


    async def event_generator():
        async for event in workflow.astream(initial_state):
            node_name = list(event.keys())[0]
            state = event[node_name]
            response = {
                "node": node_name,
                "status": NODE_STATUS.get(node_name, node_name),
                "data": None
            }
            if node_name == "research":
                response["data"] = state["research"]

            elif node_name == "topic":
                response["data"] = [
                    idea.title
                    for idea in state["ideas"].ideas
                ]

            elif node_name == "script":
                script = state["script"]
                response["data"] = {
                    "hook": script.hook,
                    "body": script.body,
                    "ending": script.ending,
                    "cta": script.cta
                }

            elif node_name == "evaluator":
                evaluation = state["evaluation"]
                response["data"] = {
                    "quality": evaluation.quality,
                    "feedback": evaluation.feedback,
                    "retry_count": state.get('retry_count'),
                    "max_retry_count":3
                }
            yield f"data: {json.dumps(response)}\n\n"


    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream"
    )
