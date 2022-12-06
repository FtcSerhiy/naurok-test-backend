from dataclasses import dataclass

@dataclass
class Key:
    name: str
    response: list

    def __init__(self, name: str, response: str):
        self.name = name
        self.response = response
