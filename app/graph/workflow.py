from langgraph.graph import START, END, StateGraph

from app.graph.state import GraphState
from app.graph.nodes import (
    research_node,
    topic_node,
    script_node,
)

graph = StateGraph(GraphState)

graph.add_node("research", research_node)
graph.add_node("topic", topic_node)
graph.add_node("script", script_node)

graph.add_edge(START, "research")
graph.add_edge("research", "topic")
graph.add_edge("topic", "script")
graph.add_edge("script", END)

workflow = graph.compile()