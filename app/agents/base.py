from app.llm import get_llm
from app.prompts.manager import PromptManager


class BaseAgent:

    prompt_name = None

    def __init__(self):
        self.llm = get_llm()
        self.prompt_manager = PromptManager()

    @property
    def prompt(self) -> str:
        if not self.prompt_name:
            raise ValueError("prompt_name is not defined.")
        return self.prompt_manager.load(self.prompt_name)