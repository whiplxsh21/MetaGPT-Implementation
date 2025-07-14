from dataclasses import dataclass

@dataclass
class Task:
    description: str
    context: str = ""
    metadata: dict = None
