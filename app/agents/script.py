from app.agents.base import BaseAgent
from app.schemas.script import ScriptResponse


class ScriptAgent(BaseAgent):

    prompt_name = "script"

    def run(
            self,
            research,
            topic,
            previous_script=None,
            feedback=None,
    ):
        prompt = self.prompt.format(
            research=research,
            topic=topic,
            previous_script=previous_script or "",
            feedback=feedback or "",
        )

        structured_llm = self.llm.with_structured_output(
            ScriptResponse
        )

        return structured_llm.invoke(prompt)