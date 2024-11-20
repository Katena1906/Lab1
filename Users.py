from Books import Book
from typing import List

class User:
    def __init__(self, username:str, email:str):
        self.username: str = username
        self.email: str = email
        self.purchased: List[Book] = []

    def purchase(self, book: Book) -> None:
        self.purchased.append(book)
        print(f"{self.username} purchased '{book.title}'.")

    def list_purchased_books(self) -> None:
        if not self.purchased:
            print(f"{self.username} has not purchased any books.")
            return
        print(f"{self.username}'s purchased books:")
        for book in self.purchased:
            print(f"- {book.title} by {book.author.name} {book.author.lastname}")

