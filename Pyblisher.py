import json
from typing import List
from Books import Book

class Publisher:
    def __init__(self, name: str):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Publisher name must be a non-empty string.")
        self.__name = name
        self.__books: List[Book] = []

    def publish_book(self, book: Book):
        if not isinstance(book, Book):
            raise ValueError("Must be class Book")
        if book in self.__books:
            raise ValueError(f"The book '{book.title}' is already published.")
        self.__books.append(book)
        print(f"Book '{book.title}' has been published by {self.__name}.")


    def to_json(self) -> dict:
        return {"name": self.__name,
                "books": [book.to_json() for book in self.__books]}

    @classmethod
    def from_json(cls, data: dict):
        publisher = cls(name=data["name"])
        [Book.from_json(book) for book in data["books"]]
        return publisher

