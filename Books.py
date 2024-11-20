from Author import Author
class Book:
    def __init__(self, title: str,isbn: int, price: float, genre: str, author: Author)-> None:
        self.title: str = title
        self.isbn: int = isbn
        self.price: float = price
        self.genre: str = genre
        self.author: Author = author

    def info(self) -> None:
        print(f"Title: {self.title}\nISBN: {self.isbn}\nPrice: {self.price}\nGenre: {self.genre}\nAuthor: {self.author.name} {self.author.lastname}")
