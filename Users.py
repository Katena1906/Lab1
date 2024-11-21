from Books import Book
from typing import List
import json

class User:
    def __init__(self, username: str, email: str):
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

    def to_json(self) -> str:
        return json.dumps({
            'username': self.username,
            'email': self.email,
            'purchased': [book.title for book in self.purchased]
        })

    def save_to_file(self, filename: str) -> None:
        json_str = self.to_json()
        with open(filename, 'w', encoding='utf-8') as save_file:
            save_file.write(json_str)

    @classmethod
    def from_json(cls, json_str: str) -> 'User ':
        data = json.loads(json_str)
        user = cls(data['username'], data['email'])
        return user

    @classmethod
    def load_from_file(cls, filename: str) -> 'User ':
        with open(filename, 'r', encoding='utf-8') as file:
            json_str = file.read()
            return cls.from_json(json_str)