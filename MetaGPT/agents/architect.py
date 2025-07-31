from .base_agent import BaseAgent

class ArchitectAgent(BaseAgent):
    def run(self, task):
        prompt = (
            "As a Software Architect, design the system for the following project. "
            "Decompose the system into modules/components, define interfaces, and provide a high-level architecture diagram (textual). Use the following format:\n"
            "## Architecture Overview\n- ...\n\n## Modules/Components\n- ...\n\n## Interfaces\n- ...\n\n## Architecture Diagram\n- ...\n\n"
            f"Task Breakdown and Schedule:\n{task.context}"
        )
        return self.llm.generate(prompt)
