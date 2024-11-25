
class Author:
    def __init__(self, name: str, lastname: str):
        if not isinstance(name, str):
            raise TypeError("Name must be string")
        if not isinstance(lastname, str):
            raise TypeError("Lastname must be string")
        self.__name: str = name
        self.__lastname: str = lastname

    def to_json(self) -> dict:
        return {"name": self.__name, "lastname": self.__lastname}

    @classmethod
    def from_json(cls, data: dict):
        return cls(name=data["name"], lastname=data["lastname"])