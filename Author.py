from Books import Book
from typing import List

class Author:
    def __init__(self, name:str):
        self.name: str = name
        self.books: List[Book]=[]

    def list_book(self) -> None:
        for book in self.books:
            print(f"Name:{book.title}, price:{book.price}")

    def add_book(self, book: Book) -> None:
        self.books.append(book)