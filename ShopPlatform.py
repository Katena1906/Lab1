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

    def remove_user(self, user: User) -> None:
        if not isinstance(user, User):
           raise TypeError("Expected user instance")
        try:
            self.users.remove(user)
            print(f"{user.username} removed")
        except ValueError:
            print(f"'{user.username} not in platform")

    def remove_book(self, book: Book) -> None:
        if not isinstance(book, Book):
            raise TypeError("Expected Book instance")
        try:
            self.books.remove(book)
            print(f"'{book.title}' removed from platform")
        except ValueError:
            print(f"'{book.title}' not in platform")

    def find_book(self,title: str) -> None:
        found = False
        for book in self.books:
            if title==book.title:
                print(f"Book {title} found")
                found = True
                break
        if not found:
            print(f"Book {title} not found")
