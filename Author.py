import json
class Author:
    def __init__(self, name: str, lastname: str):
        self.name: str = name
        self.lastname: str = lastname

    def to_dict(self) -> dict:
        return {"name": self.name, "lastname": self.lastname}

    @classmethod
    def from_dict(cls, data: dict):
        return cls(name=data["name"], lastname=data["lastname"])


    def info(self) -> None:
        print(
            f"Name: {self.name}\nLastname: {self.lastname}")

    def to_json(self) -> str:
        return json.dumps({
            'name': self.name,
            'lastname': self.lastname
        })

    def save_to_file(self, filename: str) -> None:
        json_str = self.to_json()
        with open(filename, 'w', encoding='utf-8') as save_file:
            save_file.write(json_str)
