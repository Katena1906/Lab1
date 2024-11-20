from Author import Author
class Book:
    def __init__(self, title:str, author:Author,isbn:int, price:float, genre:str )-> None:
        self.title: str = title
        self.author: Author = author
        self.isbn: int = isbn
        self.price: float = price
        self.genre: str =genre


