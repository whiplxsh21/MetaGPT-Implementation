from .base_agent import BaseAgent

class ProductManagerAgent(BaseAgent):
    def run(self, task):
        prompt = (
            "As a Product Manager, analyze the following project idea. "
            "Write clear product requirements, construct user scenarios, and provide user stories in the following format:\n"
            "## Product Requirements\n- ...\n\n## User Scenarios\n- ...\n\n## User Stories\n- ...\n\n"
            f"Project Idea:\n{task.description}"
        )
        return self.llm.generate(prompt)
