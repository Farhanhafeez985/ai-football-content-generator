import streamlit as st
import html


def render_agent_card(
    title: str,
    icon: str,
    status: str,
    body: str = "",
):

    body = body.replace("\n", "<br>")


    st.markdown(
        f"""
<details class="agent-card">

<summary>

<div class="agent-header">

<div class="agent-title">
{icon} {title}
</div>

<div class="agent-status">
{status}
</div>

</div>

</summary>

<div class="agent-body">
    {body}
</div>

</details>
""",
        unsafe_allow_html=True,
    )