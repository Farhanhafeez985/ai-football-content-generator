from app.agents.base import BaseAgent
from app.tools import TOOLS
from langchain.agents import create_agent

class ResearchAgent(BaseAgent):
    prompt_name = "research"

    def __init__(self):
        super().__init__()
        self.agent = create_agent(
            model=self.llm,
            tools=TOOLS,
            system_prompt=self.prompt_manager.load("research"),
            debug=True,
        )

    def run(self, topic):
        response = self.agent.invoke(
            {
                "messages": [
                    {"role": "user", "content": topic}
                ]
            }
        )

        return response["messages"][-1].content