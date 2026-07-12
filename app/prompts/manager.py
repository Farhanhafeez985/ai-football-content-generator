from pathlib import Path


class PromptManager:

    def __init__(self):
        self.prompt_dir = Path("app/prompts")

    def load(self, name: str) -> str:
        prompt_file = self.prompt_dir / f"{name}.txt"
        return prompt_file.read_text(encoding="utf-8")