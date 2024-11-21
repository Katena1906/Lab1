from Users import User
from Books import Book
from typing import List


class Cart:
    def __init__(self, user: User):
        self.user: User = user
        self.items: List[Book] = []

    def add_book(self, book: Book) -> None:
        if not isinstance(book, Book):
            raise TypeError("Expected Book instance")
        self.items.append(book)
        print(f"'{book.title}' added to {self.user.username} cart")

    def remove_book(self, book: Book) -> None:
        if not isinstance(book, Book):
            raise TypeError("Expected Book instance")
        try:
            self.items.remove(book)
            print(f"'{book.title}' removed from {self.user.username} cart")
        except ValueError:
            print(f"'{book.title}' is not in {self.user.username} cart")

    def list_items(self) -> None:
        if not self.items:
            print(f"{self.user.username} cart is empty")
            return
        print(f"Books in {self.user.username} cart:")
        for book in self.items:
            print(f"- {book.title} by {book.author.name} {book.author.lastname}")

    def total_price(self) -> float:
        total = sum(book.price for book in self.items)
        return total


class Order:
    def __init__(self, order_id: str,user: User):
        self.order_id: str = order_id
        self.user: User = user
        self.status: str = "processing"
        self.in_order: List[Book] = []

    def add_book_to_order(self, book: Book) -> None:
        if not isinstance(book, Book):
            raise TypeError("Expected Book instance")
        self.in_order.append(book)
        print(f"'{book.title}' added to {self.user.username} order")

    def remove_book_in_order(self, book: Book) -> None:
        if not isinstance(book, Book):
            raise TypeError("Expected Book instance")
        try:
            self.in_order.remove(book)
            print(f"'{book.title}' removed from {self.user.username} order")
        except ValueError:
            print(f"'{book.title}' is not in {self.user.username} order")

    def list_items(self) -> None:
        if not self.in_order:
            print(f"{self.user.username} order is empty")
            return
        print(f"Books in {self.user.username} cart:")
        for book in self.in_order:
            print(f"- {book.title} by {book.author.name} {book.author.lastname}")

    def total_price(self) -> float:
        total = sum(book.price for book in self.in_order)
        return total

    def change_status(self, new_status: str) -> None:
        valid_statuses = ["processing", "shipped", "delivered", "canceled"]
        if new_status not in valid_statuses:
            raise ValueError(f"Invalid status: {new_status}. Valid statuses are: {', '.join(valid_statuses)}.")
        self.status = new_status
        print(f"Order status changed to '{self.status}'")