from app.agents.base import BaseAgent
from app.schemas.script import ScriptResponse


class ScriptAgent(BaseAgent):

    prompt_name = "script"

    def run(self,research, topic):
        prompt = self.prompt.format(
            research=research,
            topic=topic
        )

        structured_llm = self.llm.with_structured_output(
            ScriptResponse
        )

        return structured_llm.invoke(prompt)