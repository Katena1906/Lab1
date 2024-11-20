from Books import Book
from Users import User
from typing import List

class ShopPlatform:
    def __init__(self):
        self.users: List[User] = []
        self.books: List[Book] = []

    def add_user(self, user: User) -> None:
        if not isinstance(user, User):
            raise TypeError("Expected user instance")
        self.users.append(user)
        print(f"{user.username} added")

    def add_book(self, book: Book) -> None:
        if not isinstance(book, Book):
            raise TypeError("Expected book instance")
        self.books.append(book)
        print(f"{book.title} added")
