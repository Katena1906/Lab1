class Author:
    def __init__(self, name:str, lastname:str):
        self.name: str = name
        self.lastname: str = lastname

    def info(self) -> None:
        print(
            f"Name: {self.name}\nLastname: {self.lastname}")