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

    def to_json(self) -> dict:
        return {
            'user': self.user.username,
            'book': self.book.title,
            'comment': self.comment,
            'rating': self.rating
        }

