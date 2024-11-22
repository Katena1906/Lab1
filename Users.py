from Books import Book
from typing import List

class User:
    def __init__(self, username: str, email: str):
        if not isinstance(username, str) or not username.strip():
            raise ValueError("Username must be a non-empty string.")
        if not isinstance(email, str) or "@" not in email or "." not in email:
            raise ValueError("Email must be a valid email address.")
        self.username: str = username
        self.email: str = email
        self.purchased: List[Book] = []

    def purchase(self, book: Book) -> None:
        self.purchased.append(book)
        print(f"{self.username} purchased '{book.title}'.")

    def list_purchased_books(self) -> None:
        if not self.purchased:
            print(f"{self.username}  not purchased any books")
            return
        print(f"{self.username} purchased books:")
        for book in self.purchased:
            print(f"- {book.title} by {book.author.name} {book.author.lastname}")

    def to_json(self) -> dict:
        return {
            "username": self.username,
            "email": self.email,
            "purchased": [book.to_json() for book in self.purchased],
        }

    @classmethod
    def from_json(cls, data: dict):
        user = cls(username=data["username"], email=data["email"])
        user.purchased = [Book.from_json(book) for book in data["purchased"]]
        return user

