from langgraph.graph import StateGraph, END

from app.graph.state import GraphState
from app.graph.nodes import (
    supervisor_node,
    research_node,
    topic_node,
    script_node,
    evaluator_node,
    voice_node,
)

workflow = StateGraph(GraphState)

# ----------------------------
# Nodes
# ----------------------------

workflow.add_node(
    "supervisor",
    supervisor_node
)

workflow.add_node(
    "research",
    research_node
)

workflow.add_node(
    "topic",
    topic_node
)

workflow.add_node(
    "script",
    script_node
)

workflow.add_node(
    "evaluator",
    evaluator_node
)

workflow.add_node(
    "voice",
    voice_node,
)

# ----------------------------
# Entry Point
# ----------------------------

workflow.set_entry_point(
    "supervisor"
)


# ----------------------------
# Routing
# ----------------------------

def route(state):
    return state["next_agent"]


workflow.add_conditional_edges(
    "supervisor",
    route,
    {
        "research": "research",
        "topic": "topic",
        "script": "script",
        "voice": "voice",
        "finish": END,
    }
)

# ----------------------------
# Fixed Edges
# ----------------------------

workflow.add_edge(
    "research",
    "supervisor"
)

workflow.add_edge(
    "topic",
    "supervisor"
)

workflow.add_edge(
    "script",
    "evaluator"
)

# Evaluator finishes its work,
# then Supervisor decides what to do next.
workflow.add_edge(
    "evaluator",
    "supervisor",
)

# Voice generation complete,
# then Supervisor decides to finish.
workflow.add_edge(
    "voice",
    "supervisor",
)

workflow = workflow.compile()