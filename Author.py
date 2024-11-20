from Books import Book
from typing import List

class Author:
    def __init__(self, name:str):
        self.name: str = name
        self.books: List[Book]=[]

    def list_books(self) -> None:
        if not self.books:
            print(f"{self.name} has no books.")
            return
        for book in self.books:
            print(f"Title: {book.title}, Price: {book.price}, Genre: {book.genre}")

    def add_book(self, book: Book) -> None:
        self.books.append(book)