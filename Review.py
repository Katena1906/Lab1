from Users import User
from Books import Book

class Review:
    def __init__(self, user: User, book: Book, comment: str, rating: int):
        self.user: User = user
        self.book: Book = book
        self.comment: str = comment
        self.rating: int = rating

