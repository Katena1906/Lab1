from Books import Book
from typing import List

class User:
    def __init__(self, username:str, email:str):
        self.username: str = username
        self.email: str = email
        self.purchased: List[Book] = []