from .base_agent import BaseAgent

class EngineerAgent(BaseAgent):
    def run(self, task):
        prompt = (
            "As an Engineer, implement the modules/components described below. "
            "Provide code for each module/component, following best practices. Use the following format:\n"
            "## Module: <Name>\n``````\n\n"
            f"Architecture and Interface Definitions:\n{task.context}"
        )
        return self.llm.generate(prompt)
