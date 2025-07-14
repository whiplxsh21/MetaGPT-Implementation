from agents.product_manager import ProductManagerAgent
from agents.project_manager import ProjectManagerAgent
from agents.architect import ArchitectAgent
from agents.engineer import EngineerAgent
from agents.qa_engineer import QAEngineerAgent
from llm.groq_llm import GroqLLM
from .task import Task

class Pipeline:
    def __init__(self):
        self.llm = GroqLLM()
        self.pm = ProductManagerAgent(self.llm)
        self.projm = ProjectManagerAgent(self.llm)
        self.architect = ArchitectAgent(self.llm)
        self.engineer = EngineerAgent(self.llm)
        self.qa = QAEngineerAgent(self.llm)

    def run(self, user_input):
        task = Task(description=user_input)
        requirements = self.pm.run(task)
        proj_task = Task(description=user_input, context=requirements)
        project_plan = self.projm.run(proj_task)
        arch_task = Task(description=user_input, context=project_plan)
        architecture = self.architect.run(arch_task)
        eng_task = Task(description=user_input, context=architecture)
        code = self.engineer.run(eng_task)
        qa_task = Task(description=user_input, context=code)
        qa_report = self.qa.run(qa_task)
        return {
            "requirements": requirements,
            "project_plan": project_plan,
            "architecture": architecture,
            "code": code,
            "qa_report": qa_report
        }
