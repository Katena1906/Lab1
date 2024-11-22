# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from Author import Author
from Books import Book
from Users import User
from Cart import Cart, Order
from Review import Review
from ShopPlatform import ShopPlatform
import json

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Создание данных
    author = Author("Sui", "Ishida")
    book = Book("Tokyo Ghoul", 123456, 12.99, "Psyhology drama", author)
    user = User("Vovchik", "VovchikPomidorchik@mail.com")
    review = Review(user, book, "Great book!", 5)
    cart = Cart(user)
    cart.add_book(book)
    order = Order("order123", user)
    order.add_book_to_order(book)

    # Создание платформы
    platform = ShopPlatform()
    platform.add_user(user)
    platform.add_book(book)
    platform.add_order(order)
    platform.add_cart(cart)
    platform.reviews.append(review)

    with open("platform.json", "w", encoding="utf-8") as out_file:
        json.dump(platform.to_json(), out_file, ensure_ascii=False, indent=4)


    with open("platform.json", "r", encoding="utf-8") as inp_file:
        data = json.load(inp_file)
        loaded_platform = ShopPlatform.from_json(data)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
