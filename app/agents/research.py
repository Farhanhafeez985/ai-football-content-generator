from app.agents.base import BaseAgent
from app.tools import TOOLS



class ResearchAgent(BaseAgent):

    prompt_name = "research"

    def run(self, topic):
        search_results = TOOLS[0].invoke(topic)

        prompt = self.prompt_manager.load("research").format(
            topic=topic,
            search_results=search_results,
        )
        response = self.llm.invoke(prompt)
        return response.content