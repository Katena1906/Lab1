from Books import Book
from Users import User
from Review import Review
from typing import List
from Cart import Cart, Order
from Coupon import Coupon
from Payment import Payment
from Pyblisher import Publisher


class ShopPlatform:
    def __init__(self):
        self.__users: List[User] = []
        self.__books: List[Book] = []
        self.__orders: List[Order] = []
        self.__carts: List[Cart] = []
        self.__reviews: List[Review] = []
        self.__coupons: List[Coupon] = []
        self.__payments: List[Payment] = []
        self.__publishers: List[Publisher] = []

    def add_publisher(self,publisher: Publisher):
        if not isinstance(publisher, Publisher):
            raise TypeError("Argument must be an instance of the Publisher class")
        self.__publishers.append(publisher)
        print(f"Publisher added successfully")

    def add_payment(self, payment: Payment):
        if not isinstance(payment, Payment):
            raise TypeError("Argument must be an instance of the Payment class")
        self.__payments.append(payment)
        print(f"Payment  added successfully")

    def add_coupon(self, coupon: Coupon):
        if not isinstance(coupon, Coupon):
            raise TypeError("Argument must be an instance of the Coupon class")
        if any(existing_coupon.code == coupon.code for existing_coupon in self.__coupons):
            print(f"User with coupon code {coupon.code} already exists")
            return
        self.__coupons.append(coupon)
        print(f"Coupon {coupon.code} added")

    def add_user(self, user: User):
        if not isinstance(user, User):
            raise TypeError("Argument must be an instance of the User class.")
        if any(existing_user.email == user.email for existing_user in self.__users):
            print(f"User with email {user.email} already exists")
            return
        self.__users.append(user)
        print(f"User {user.username} added")

    def add_book(self, book: Book):
        if not isinstance(book, Book):
            raise TypeError("Argument must be an instance of the Book class.")
        if any(existing_book.isbn == book.isbn for existing_book in self.__books):
            print(f"Book with ISBN {book.isbn} already exists")
            return
        self.__books.append(book)
        print(f"Book '{book.title}' added")

    def add_order(self, order: Order):
        if not isinstance(order, Order):
            raise TypeError("Argument must be an instance of the Order class.")
        if any(existing_order.order_id == order.order_id for existing_order in self.__orders):
            print(f"Order with ID {order.order_id} already exists")
            return
        self.__orders.append(order)
        print(f"Order {order.order_id} added")

    def add_cart(self, cart: Cart):
        if not isinstance(cart, Cart):
            raise TypeError("Argument must be an instance of the Cart class.")
        if any(existing_cart.user.email == cart.user.email for existing_cart in self.__carts):
            print(f"Cart for user {cart.user.username} already exists")
            return
        self.__carts.append(cart)
        print(f"Cart for user {cart.user.username} added")

    def add_review(self, review: Review):
        if not isinstance(review, Review):
            raise TypeError("Argument must be an instance of the Review class.")
        if any(
            existing_review.user.email == review.user.email and
            existing_review.book.isbn == review.book.isbn
            for existing_review in self.__reviews
        ):
            print(f"Review for book '{review.book.title}' by user {review.user.username} already exists")
            return
        self.__reviews.append(review)
        print(f"Review by {review.user.username} for book '{review.book.title}' added")

    def to_json(self) -> dict:
        return {"users": [user.to_json() for user in self.__users],
                "books": [book.to_json() for book in self.__books],
                "carts": [cart.to_json() for cart in self.__carts],
                "orders": [order.to_json() for order in self.__orders],
                "reviews": [review.to_json() for review in self.__reviews],
                "coupons": [coupon.to_json() for coupon in self.__coupons],
                "payments": [payment.to_json() for payment in self.__payments],
                "publishers": [publisher.to_json() for publisher in self.__publishers]}

    @classmethod
    def from_json(cls, data: dict):
        platform = cls()
        platform.users = [User.from_json(user) for user in data["users"]]
        platform.books = [Book.from_json(book) for book in data["books"]]
        platform.orders = [Order.from_json(order) for order in data["orders"]]
        platform.carts = [Cart.from_json(cart) for cart in data["carts"]]
        platform.reviews = [Review.from_json(review) for review in data["reviews"]]
        platform.coupons = [Coupon.from_json(coupon) for coupon in data["coupons"]]
        platform.payments = [Payment.from_json(payment) for payment in data["payments"]]
        platform.publishers = [Publisher.from_json(publisher) for publisher in data["publishers"]]
        return platform


