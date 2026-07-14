import streamlit as st

from components.agent_card import render_agent_card
from utils.constants import STATUS


def render_chat():

    st.title("⚽ AI Football Studio")

    research = st.empty()
    topic = st.empty()
    script = st.empty()
    # evaluation = st.empty()

    with research.container():

        render_agent_card(
            "Research Agent",
            "🔍",
            STATUS["waiting"]
        )

    with topic.container():

        render_agent_card(
            "Topic Generator",
            "💡",
            STATUS["waiting"]
        )

    with script.container():

        render_agent_card(
            "Script Writer",
            "✍️",
            STATUS["waiting"]
        )

    # with evaluation.container():
    #
    #     render_agent_card(
    #         "Evaluator",
    #         "🧐",
    #         STATUS["waiting"]
    #     )

    return {
        "research": research,
        "topic": topic,
        "script": script,
    }