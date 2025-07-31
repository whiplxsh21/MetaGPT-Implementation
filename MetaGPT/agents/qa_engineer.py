from .base_agent import BaseAgent

class QAEngineerAgent(BaseAgent):
    def run(self, task):
        prompt = (
            "As a QA Engineer, generate test cases for the following implementation. "
            "Provide test cases, validation strategies, and a bug report template in the following format:\n"
            "## Test Cases\n- ...\n\n## Validation Strategies\n- ...\n\n## Bug Report Template\n- ...\n\n"
            f"Implementation Code:\n{task.context}"
        )
        return self.llm.generate(prompt)
