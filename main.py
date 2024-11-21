# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from Author import Author
from Books import Book
from Users import User
from Cart import Cart
from Review import Review

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':


    author = Author(name="George", lastname="Orwell")


    book1 = Book(title="1984", isbn=1234567890, price=9.99, genre="Dystopian", author=author)
    book2 = Book(title="Animal Farm", isbn=1234567891, price=7.99, genre="Political Satire", author=author)

    user = User("john_doe", "john@example.com")

    cart = Cart(user)
    cart.add_book(book1)
    cart.add_book(book2)


    available_books = [book1, book2]


    author = Author("John", "Doe")
    book = Book("Example Book", 2236667890, 29.99, "Fiction", author)
    user = User("johndoe", "johndoe@example.com")
    review = Review(user, book, "Great read!", 5)
    review.read_review()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
