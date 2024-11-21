import json
class Author:
    def __init__(self, name: str, lastname: str):
        self.name: str = name
        self.lastname: str = lastname

    def to_json(self) -> dict:
        return {"name": self.name, "lastname": self.lastname}

    @classmethod
    def from_json(cls, data: dict):
        return cls(name=data["name"], lastname=data["lastname"])