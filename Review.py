from Users import User
from Books import Book
import json

class Review:
    def __init__(self, user: User, book: Book, comment: str, rating: int):
        self.user: User = user
        self.book: Book = book
        self.comment: str = comment
        self.rating: int = rating
        if rating < 1 or rating > 5:
            raise ValueError("Rating must be between 1 and 5.")

    def read_review(self) -> None:
        print(f"User:{self.user} wrote {self.comment} and gave rating {self.rating} for the book '{self.book.title}'")

    def to_json(self) -> str:
        return json.dumps({
            'user': self.user.username,
            'book': self.book.title,
            'comment': self.comment,
            'rating': self.rating
        })

    def save_to_file(self, filename: str) -> None:
        json_str = self.to_json()
        with open(filename, 'w', encoding='utf-8') as save_file:
            save_file.write(json_str)

    @classmethod
    def from_json(cls, json_str: str, user: User, book: Book) -> 'Review':
        data = json.loads(json_str)
        return cls(user, book, data['comment'], data['rating'])

    @classmethod
    def load_from_file(cls, filename: str, user: User, book: Book) -> 'Review':
        with open(filename, 'r', encoding='utf-8') as file:
            json_str = file.read()
            return cls.from_json(json_str, user, book)