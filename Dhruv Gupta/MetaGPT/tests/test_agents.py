import pytest
from agents.base_agent import BaseAgent
from core.task import Task

class DummyLLM:
    def generate(self, prompt):
        return f"Response to: {prompt}"

class DummyAgent(BaseAgent):
    def run(self, task):
        return self.llm.generate(task.description)

def test_base_agent_run():
    llm = DummyLLM()
    agent = DummyAgent(llm)
    task = Task(description="Test task")
    output = agent.run(task)
    assert "Test task" in output
