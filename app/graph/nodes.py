from app.agents.research import ResearchAgent
from app.agents.topic import TopicAgent
from app.agents.script import ScriptAgent

from app.graph.state import GraphState


research_agent = ResearchAgent()
topic_agent = TopicAgent()
script_agent = ScriptAgent()


def research_node(state: GraphState):
    research = research_agent.run(state["topic"])

    return {
        "research": research
    }


def topic_node(state: GraphState):
    ideas = topic_agent.run(state["research"])

    return {
        "ideas": ideas
    }


def script_node(state: GraphState):
    selected_topic = state["ideas"].ideas[0].title

    script = script_agent.run(selected_topic)

    return {
        "script": script
    }