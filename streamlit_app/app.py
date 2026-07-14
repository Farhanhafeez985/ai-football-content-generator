import streamlit as st

from utils.api import stream_response
from components.agent_card import render_agent_card
from components.sidebar import render_sidebar
from components.chat import render_chat

st.set_page_config(
    page_title="AI Football Studio",
    page_icon="⚽",
    layout="wide",
)

with open("assets/style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True,
    )

render_sidebar()

placeholders = render_chat()

# Holds the latest generated script until evaluator approves it
pending_script = None

prompt = st.chat_input("Ask anything about football...")

if prompt:

    st.markdown(
        f"""
    <div class="user-message">
        <div class="user-bubble">
            {prompt}
        </div>
        <div class="user-avatar">
            F
        </div>
    </div>
    """,
        unsafe_allow_html=True,
    )

    for event in stream_response(prompt):

        node = event["node"]

        # --------------------------------------------------
        # Research
        # --------------------------------------------------
        if node == "research":

            with placeholders["research"].container():
                render_agent_card(
                    title="Research Agent",
                    icon="🔍",
                    status="🟢 Complete",
                    body=event["data"],
                )

        # --------------------------------------------------
        # Topic
        # --------------------------------------------------
        elif node == "topic":

            with placeholders["topic"].container():
                render_agent_card(
                    title="Topic Generator",
                    icon="💡",
                    status="🟢 Complete",
                    body="\n".join(
                        f"• {idea}" for idea in event["data"]
                    ),
                )

            # Start script generation
            with placeholders["script"].container():
                render_agent_card(
                    title="Script Writer",
                    icon="✍️",
                    status="🟡 Generating...",
                    body="Creating the first draft...",
                )

        # --------------------------------------------------
        # Script (store only)
        # --------------------------------------------------
        elif node == "script":

            pending_script = event["data"]

        # --------------------------------------------------
        # Evaluator (controls Script UI)
        # --------------------------------------------------
        elif node == "evaluator":

            evaluation = event["data"]

            quality = evaluation["quality"].lower()
            retry = evaluation["retry_count"]
            max_retry = evaluation["max_retry_count"]

            # -------- Script Approved --------
            if quality == "good":

                body = f"""
### 🎣 Hook

{pending_script["hook"]}

---

### 📝 Body

{pending_script["body"]}

---

### 🎬 Ending

{pending_script["ending"]}

---

### 📢 Call To Action

{pending_script["cta"]}
"""

                with placeholders["script"].container():
                    render_agent_card(
                        title="Script Writer",
                        icon="✍️",
                        status="🟢 Complete",
                        body=body,
                    )

            # -------- Retry --------
            elif retry < max_retry:

                with placeholders["script"].container():
                    render_agent_card(
                        title="Script Writer",
                        icon="✍️",
                        status=f"🟡 Regenerating... ({retry + 1}/{max_retry})",
                        body=evaluation["feedback"],
                    )

            # -------- Max retries --------
            else:

                body = f"""
⚠️ **Maximum retries reached.**

Showing the best available script.

---

### 🎣 Hook

{pending_script["hook"]}

---

### 📝 Body

{pending_script["body"]}

---

### 🎬 Ending

{pending_script["ending"]}

---

### 📢 Call To Action

{pending_script["cta"]}
"""

                with placeholders["script"].container():
                    render_agent_card(
                        title="Script Writer",
                        icon="✍️",
                        status="🟠 Max Retries Reached",
                        body=body,
                    )