from app.agents.base import BaseAgent
from app.schemas.supervisor import SupervisorDecision
from app.config import settings

class SupervisorAgent(BaseAgent):

    prompt_name = "supervisor"
    DEBUG_EVALUATION = True
    def run(self, state):

        prompt = self.prompt.format(
            evaluation=state.get("evaluation")
        )

        structured_llm = self.llm.with_structured_output(
            SupervisorDecision
        )

        decision = structured_llm.invoke(prompt)

        # Normalize legacy value
        if decision.next_agent == "evaluate":
            decision.next_agent = "evaluator"

        # ----------------------------
        # Safety Routing
        # ----------------------------

        if not state.get("research"):
            decision.next_agent = "research"

        elif not state.get("ideas"):
            decision.next_agent = "topic"

        elif not state.get("script"):
            decision.next_agent = "script"

        elif not state.get("evaluation"):
            decision.next_agent = "evaluator"

        # Audio already generated -> Finish
        elif state.get("audio_path"):
            decision.next_agent = "finish"

        # Evaluation completed
        elif state.get("evaluation"):

            if (
                state["evaluation"].quality == "poor"
                and state.get("retry_count", 0) < settings.MAX_SCRIPT_RETRIES
            ):
                decision.next_agent = "script"

            elif (
                state["evaluation"].quality == "good"
                and not state.get("audio_path")
            ):
                decision.next_agent = "voice"

            else:
                decision.next_agent = "finish"

        return decision