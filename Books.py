from Author import Author
import json
class Book:
    def __init__(self, title: str,isbn: int, price: float, genre: str, author: Author)-> None:
        self.title: str = title
        self.isbn: int = isbn
        self.price: float = price
        self.genre: str = genre
        self.author: Author = author

    def info(self) -> None:
        print(f"Title: {self.title}\nISBN: {self.isbn}\nPrice: {self.price}\nGenre: {self.genre}\nAuthor: {self.author.name} {self.author.lastname}")

    def to_json(self) -> str:
        return json.dumps({
            'title': self.title,
            'isbn': self.isbn,
            'price': self.price,
            'genre': self.genre,
            'author': {
                'name': self.author.name,
                'lastname': self.author.lastname
            }
        })

    def save_to_file(self, filename: str) -> None:
        json_str = self.to_json()
        with open(filename, 'w', encoding='utf-8') as save_file:
            save_file.write(json_str)

    @classmethod
    def from_json(cls, json_str: str) -> 'Book':
        data = json.loads(json_str)
        author = Author(data['author']['name'], data['author']['lastname'])
        return cls(data['title'], data['isbn'], data['price'], data['genre'], author)




