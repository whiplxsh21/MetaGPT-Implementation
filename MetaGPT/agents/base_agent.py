from abc import ABC, abstractmethod

class BaseAgent(ABC):
    def __init__(self, llm):
        self.llm = llm

    @abstractmethod
    def run(self, task):
        pass
