from Users import User
from Books import Book

class Review:
    def __init__(self, user: User, book: Book, comment: str, rating: int):
        if not isinstance(user, User):
            raise TypeError("user must be instance of User class")
        if not isinstance(book, Book):
            raise TypeError("book must be instance of Book class")
        if not isinstance(comment, str):
            raise TypeError("comment must be a string")
        if not isinstance(rating, int) or not (1 <= rating <= 5):
            raise ValueError(
            "rating must be an integer between 1 and 5")
        self.user: User = user
        self.book: Book = book
        self.__comment: str = comment
        self.__rating: int = rating

    def read_review(self) -> None:
        print(f"User:{self.user} wrote {self.__comment} and gave rating {self.__rating} for the book '{self.book.title}'")

    def to_json(self) -> dict:
        return {
            'user': self.user.to_json(),
            'book': self.book.to_json(),
            'comment': self.__comment,
            'rating': self.__rating
        }

    @classmethod
    def from_json(cls, data: dict):
        user = User.from_json(data["user"])
        book = Book.from_json(data["book"])
        return cls(user=user, book=book, comment=data["comment"], rating=data["rating"])