from app.agents.base import BaseAgent
from app.schemas.script import ScriptResponse


class ScriptAgent(BaseAgent):

    prompt_name = "script"

    def run(self, topic: str) -> ScriptResponse:
        prompt = self.prompt.format(
            topic=topic
        )

        structured_llm = self.llm.with_structured_output(
            ScriptResponse
        )

        return structured_llm.invoke(prompt)