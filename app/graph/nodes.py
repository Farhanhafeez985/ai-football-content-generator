from app.agents.supervisor import SupervisorAgent
from app.agents.research import ResearchAgent
from app.agents.topic import TopicAgent
from app.agents.script import ScriptAgent
from app.agents.evaluator import EvaluatorAgent
from app.agents.voice import VoiceAgent


supervisor_agent = SupervisorAgent()
research_agent = ResearchAgent()
topic_agent = TopicAgent()
script_agent = ScriptAgent()
evaluator_agent = EvaluatorAgent()
voice_agent = VoiceAgent()

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
        research=research,
        topic=selected_topic,
        previous_script=state.get("script"),
        feedback=(
            state["evaluation"].feedback
            if state.get("evaluation")
            else None
        ),
    )

    retry = state.get("retry_count", 0)

    # Increment only when regenerating after evaluation
    if state.get("evaluation"):
        retry += 1
    return {
        "script": script,
        "retry_count": retry,
    }

# DEBUG_EVALUATION = True  # False in production


def evaluator_node(state):

    result = evaluator_agent.run(
        state["script"]
    )
    # # Debug only
    # if DEBUG_EVALUATION:
    #     result.quality = "poor"
    #     result.feedback = "Debug mode: forcing retry."
    retry = state.get("retry_count", 0)
    return {
        "evaluation": result,
        "retry_count": retry
    }


def voice_node(state):
    script = state["script"]
    audio_path = voice_agent.run(
        narration=script.narration,
    )
    return {
        "audio_path": audio_path,
    }