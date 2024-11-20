from Users import User
from Books import Book
from typing import List

class Cart:
    def __init__(self, user: User):
        self.user: User = user
        self.items: List[Book] = []

    def add_book(self, book: Book) -> None:
        if not isinstance(book, Book):
            raise TypeError("Expected a Book instance.")
        self.items.append(book)
        print(f"'{book.title}' has been added to {self.user.username}'s cart.")

    def remove_book(self, book: Book) -> None:
        if not isinstance(book, Book):
            raise TypeError("Expected a Book instance.")
        try:
            self.items.remove(book)
            print(f"'{book.title}' has been removed from {self.user.username}'s cart.")
        except ValueError:
            print(f"'{book.title}' is not in {self.user.username}'s cart.")

    def list_items(self) -> None:
        if not self.items:
            print(f"{self.user.username}'s cart is empty.")
            return
        print(f"Books in {self.user.username}'s cart:")
        for book in self.items:
            print(f"- {book.title} by {book.author.name} {book.author.lastname}")

    def total_price(self) -> float:
        total = sum(book.price for book in self.items)
        return total