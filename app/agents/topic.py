from app.agents.base import BaseAgent
from app.schemas.topic import TopicResponse

class TopicAgent(BaseAgent):

    prompt_name = "topic"

    def run(self, research):
        prompt = self.prompt.format(
            research=research
        )

        structured_llm = self.llm.with_structured_output(TopicResponse)

        return structured_llm.invoke(prompt)