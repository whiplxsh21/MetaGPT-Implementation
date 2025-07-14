from .base_agent import BaseAgent

class ProjectManagerAgent(BaseAgent):
    def run(self, task):
        prompt = (
            "As a Project Manager, break down the following requirements and user stories into tasks. "
            "Create a project schedule, assign tasks, and provide a progress tracking table in the following format:\n"
            "## Task Breakdown\n- ...\n\n## Schedule\n- ...\n\n## Task Assignment\n- ...\n\n## Progress Tracking\n| Task | Status | Assignee |\n|------|--------|----------|\n| ...  | ...    | ...      |\n\n"
            f"Requirements and User Stories:\n{task.context}"
        )
        return self.llm.generate(prompt)
