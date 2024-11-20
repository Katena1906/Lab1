from Author import Author
class Book:
    def __init__(self, title:str, author:Author,isbn:int, price:float, genre:str )-> None:
        self.title: str = title
        self.author: Author = author
        self.isbn: int = isbn
        self.price: float = price
        self.genre: str =genre

    def info(self) -> None:
        print(
            f"Title: {self.title}\nAuthor: {self.author.name}\nISBN: {self.isbn}\nPrice: {self.price}\nGenre: {self.genre}")




