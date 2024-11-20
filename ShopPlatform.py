from Books import Book
from Users import User
from typing import List

class ShopPlatform:
    def __init__(self):
        self.users: List[User] = []
        self.books: List[Book] = []


