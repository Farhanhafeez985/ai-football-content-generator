from app.agents.base import BaseAgent
from app.schemas.evaluator import EvaluationResult


class EvaluatorAgent(BaseAgent):

    prompt_name = "evaluator"

    def run(self, script):

        prompt = self.prompt.format(
            script=script
        )

        structured_llm = self.llm.with_structured_output(
            EvaluationResult
        )

        return structured_llm.invoke(prompt)