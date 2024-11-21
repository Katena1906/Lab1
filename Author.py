import json
class Author:
    def __init__(self, name: str, lastname: str):
        self.name: str = name
        self.lastname: str = lastname

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

    @classmethod
    def from_json(cls, json_str: str) -> 'Author':
        data = json.loads(json_str)
        return cls(data['name'], data['lastname'])

    @classmethod
    def load_from_file(cls, filename: str) -> 'Author':
        with open(filename, 'r', encoding='utf-8') as file:
            json_str = file.read()
            return cls.from_json(json_str)