from app.agents.supervisor import SupervisorAgent
from app.agents.research import ResearchAgent
from app.agents.topic import TopicAgent
from app.agents.script import ScriptAgent
from app.agents.evaluator import EvaluatorAgent


supervisor_agent = SupervisorAgent()
research_agent = ResearchAgent()
topic_agent = TopicAgent()
script_agent = ScriptAgent()
evaluator_agent = EvaluatorAgent()

def supervisor_node(state):
    decision = supervisor_agent.run(state)

    print("SUPERVISOR DECISION:", decision)

    return {
        "next_agent": decision.next_agent
    }

def research_node(state):

    research = research_agent.run(
        state["topic"]
    )

    return {
        "research": research
    }


def topic_node(state):
    ideas = topic_agent.run(
        state["research"]
    )
    return {
        "ideas": ideas
    }


def script_node(state):
    research = state['research']
    selected_topic = state["ideas"].ideas[0].title

    script = script_agent.run(
        research,
        selected_topic
    )

    return {
        "script": script
    }

def evaluator_node(state):

    result = evaluator_agent.run(
        state["script"]
    )

    return {
        "evaluation": result
    }