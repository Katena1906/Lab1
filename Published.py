from Books import Book
from typing import List

class Publisher:
    def __init__(self, name: str):
        self.name: str = name
        self.books: List[Book] = []

