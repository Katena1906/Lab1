
class Book:
    def __init__(self, title:str,isbn:int, price:float, genre:str )-> None:
        self.title: str = title
        self.isbn: int = isbn
        self.price: float = price
        self.genre: str =genre

    def info(self) -> None:
        print(
            f"Title: {self.title}\nISBN: {self.isbn}\nPrice: {self.price}\nGenre: {self.genre}")
