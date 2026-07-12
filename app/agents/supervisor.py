from app.agents.base import BaseAgent
from app.schemas.supervisor import SupervisorDecision


class SupervisorAgent(BaseAgent):

    prompt_name = "supervisor"

    def run(self, state):

        prompt = self.prompt.format(
            evaluation=state.get("evaluation")
        )

        structured_llm = self.llm.with_structured_output(
            SupervisorDecision
        )

        decision = structured_llm.invoke(prompt)

        if decision.next_agent == "evaluate":
            decision.next_agent = "evaluator"

        # Safety routing

        if not state.get("research"):
            decision.next_agent = "research"

        elif state.get("research") and not state.get("ideas"):
            decision.next_agent = "topic"

        elif state.get("ideas") and not state.get("script"):
            decision.next_agent = "script"

        elif state.get("script") and not state.get("evaluation"):
            decision.next_agent = "evaluator"

        elif state.get("evaluation"):

            if state["evaluation"].quality == "poor":
                decision.next_agent = "script"

            else:
                decision.next_agent = "finish"

        return decision