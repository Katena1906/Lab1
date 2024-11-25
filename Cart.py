from Users import User
from Books import Book
from typing import List


class Cart:
    def __init__(self, user: User):
        if not isinstance(user, User):
            raise TypeError("user must be instance of User class")
        self.user: User = user
        self.__items: List[Book] = []

    def add_book(self, book: Book) -> None:
        if not isinstance(book, Book):
            raise TypeError("Expected Book instance")
        self.__items.append(book)
        print("book added to  cart")

    def remove_book(self, book: Book) -> None:
        if not isinstance(book, Book):
            raise TypeError("Expected Book instance")
        try:
            self.__items.remove(book)
            print("book removed from cart")
        except ValueError:
            print("book is not in cart")

    def list_items(self) -> None:
        if not self.__items:
            print("cart is empty")
            return
        print(f"Books in {self.user.username} cart:")
        for book in self.__items:
            print(f"{book.title}")

    def total_price(self) -> float:
        total = sum(book.price for book in self.__items)
        return total


    def to_json(self) -> dict:
        return {
            "user": self.user.to_json(),
            "items": [book.to_json() for book in self.__items],
        }

    @classmethod
    def from_json(cls, data: dict):
        user = User.from_json(data["user"])
        cart = cls(user=user)
        cart.items = [Book.from_json(book) for book in data["items"]]
        return cart


class Order:
    def __init__(self, order_id: str,user: User):
        if not isinstance(order_id, str) or not order_id.strip():
            raise ValueError("order_id must be a non-empty string")
        if not isinstance(user, User):
            raise TypeError("user must be an instance of User class")
        self.order_id: str = order_id
        self.user: User = user
        self.__status: str = "processing"
        self.__in_order: List[Book] = []

    def to_json(self) -> dict:
        return {
            "order_id": self.order_id,
            "user": self.user.to_json(),
            "status": self.__status,
            "in_order": [book.to_json() for book in self.__in_order],
        }

    @classmethod
    def from_json(cls, data: dict):
        user = User.from_json(data["user"])
        order = cls(order_id=data["order_id"], user=user)
        order.status = data["status"]
        order.in_order = [Book.from_json(book) for book in data["in_order"]]
        return order


    def add_book_to_order(self, book: Book) -> None:
        if not isinstance(book, Book):
            raise TypeError("Expected Book instance")
        self.__in_order.append(book)
        print(f"book added to {self.user.username} order")

    def remove_book_in_order(self, book: Book) -> None:
        if not isinstance(book, Book):
            raise TypeError("Expected Book instance")
        try:
            self.__in_order.remove(book)
            print(f"'book removed from {self.user.username} order")
        except ValueError:
            print(f"book is not in {self.user.username} order")

    def list_items(self) -> None:
        if not self.__in_order:
            print(f"{self.user.username} order is empty")
            return
        print(f"Books in {self.user.username} cart:")
        for book in self.__in_order:
            print(f"- {book.title}")

    def total_price(self) -> float:
        total = sum(book.price for book in self.__in_order)
        return total

    def change_status(self, new_status: str) -> None:
        valid_statuses = ["processing", "shipped", "delivered", "canceled"]
        if new_status not in valid_statuses:
            raise ValueError(f"Invalid status: {new_status}. Valid statuses are: {', '.join(valid_statuses)}.")
        self.__status = new_status
        print(f"Order status changed to '{self.__status}'")