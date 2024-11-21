from Books import Book
from Users import User
from Author import Author
from Review import Review
from typing import List
from Cart import Cart, Order

class ShopPlatform:
    def __init__(self):
        self.users: List[User] = []
        self.authors: List[Author] = []
        self.books: List[Book] = []
        self.orders: List[Order] = []
        self.carts: List[Cart] = []
        self.reviews: List[Review] = []

    def add_user(self, user: User):
        if any(existing_user.email == user.email for existing_user in self.users):
            print(f"User with email {user.email} already exists.")
            return
        self.users.append(user)
        print(f"User {user.username} added.")

    def add_book(self, book: Book):
        if any(existing_book.isbn == book.isbn for existing_book in self.books):
            print(f"Book with ISBN {book.isbn} already exists.")
            return
        self.books.append(book)
        print(f"Book '{book.title}' added.")

    def add_order(self, order: Order):
        if any(existing_order.order_id == order.order_id for existing_order in self.orders):
            print(f"Order with ID {order.order_id} already exists.")
            return
        self.orders.append(order)
        print(f"Order {order.order_id} added.")

    def add_cart(self, cart: Cart):
        if any(existing_cart.user.email == cart.user.email for existing_cart in self.carts):
            print(f"Cart for user {cart.user.username} already exists.")
            return
        self.carts.append(cart)
        print(f"Cart for user {cart.user.username} added.")

    def add_review(self, review: Review):
        if any(
            existing_review.user.email == review.user.email and
            existing_review.book.isbn == review.book.isbn
            for existing_review in self.reviews
        ):
            print(f"Review for book '{review.book.title}' by user {review.user.username} already exists.")
            return
        self.reviews.append(review)
        print(f"Review by {review.user.username} for book '{review.book.title}' added.")

    def to_json(self) -> dict:
        return {
            "users": [user.to_json() for user in self.users],
            "books": [book.to_json() for book in self.books],
            "authors": [author.to_json() for author in self.authors],
            "orders": [order.to_json() for order in self.orders],
            "carts": [cart.to_json() for cart in self.carts],
            "reviews": [review.to_json() for review in self.reviews],
        }

    @classmethod
    def from_json(cls, data: dict):
        platform = cls()
        platform.users = [User.from_json(user) for user in data["users"]]
        platform.books = [Book.from_json(book) for book in data["books"]]
        platform.authors = [Author.from_json(author) for author in data["authors"]]
        platform.orders = [Order.from_json(order) for order in data["orders"]]
        platform.carts = [Cart.from_json(cart) for cart in data["carts"]]
        platform.reviews = [Review.from_json(review) for review in data["reviews"]]
        return platform


