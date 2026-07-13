from langgraph.graph import StateGraph, END

from app.graph.state import GraphState
from app.graph.nodes import (
    supervisor_node,
    research_node,
    topic_node,
    script_node,
    evaluator_node
)

workflow = StateGraph(GraphState)

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

workflow.set_entry_point(
    "supervisor"
)


def route(state):
    return state["next_agent"]


workflow.add_conditional_edges(
    "supervisor",
    route,
    {
        "research": "research",
        "topic": "topic",
        "script": "script",
        "evaluator": "evaluator",
        "finish": END,
    }
)

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

workflow.add_edge(
    "evaluator",
    "supervisor"
)

workflow = workflow.compile()