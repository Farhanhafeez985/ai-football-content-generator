import streamlit as st


def render_sidebar():

    with st.sidebar:

        st.title("⚽ AI Football Studio")

        st.button(
            "➕ New Chat",
            use_container_width=True
        )

        st.divider()

        st.caption("Today")

        st.button(
            "🏆 UEFA Champions League Final",
            use_container_width=True
        )

        st.button(
            "⚽ Messi Story",
            use_container_width=True
        )