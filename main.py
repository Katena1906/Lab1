# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from Books import Book
from Users import User
from Review import Review
from Author import Author
from Cart import Cart, Order
from Coupon import Coupon
from Payment import Payment
from Pyblisher import Publisher
from ShopPlatform import ShopPlatform
import json

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Создание данных
    try:
        author = Author("Sui", "Ishida")
    except (ValueError, TypeError) as e:
        print(f"Error while creating Author: {e}")

    try:
        book = Book("Tokyo Ghoul", 123456, 12.99, "Psychology drama", author)
    except (TypeError, ValueError) as e:
        print(f"Error while creating Book: {e}")

    try:
        user = User("Vovchik", "VovchikPomidorchik@mail.com")
    except (ValueError, TypeError) as e:
        print(f"Error while creating User: {e}")

    try:
        review = Review(user, book, "Great book!", 5)
    except (ValueError, TypeError) as e:
        print(f"Error while creating Review: {e}")

    try:
        coupon = Coupon("ee3he38", 20.99)
    except (TypeError, ValueError) as e:
        print(f"Error while creating Coupon: {e}")

    try:
        cart = Cart(user)
        cart.add_book(book)
    except (TypeError, ValueError) as e:
        print(f"Error while creating Cart or adding book: {e}")

    try:
        order = Order("order123", user)
        order.add_book_to_order(book)
    except (TypeError, ValueError) as e:
        print(f"Error while creating Order or adding book to order: {e}")

    try:
        payment = Payment(order, "spb")
    except (TypeError, ValueError) as e:
        print(f"Error while creating Payment: {e}")

    try:
        publisher = Publisher("Weekly Shonen Jump")
        publisher.publish_book(book)
    except (ValueError, TypeError) as e:
        print(f"Error while creating Publisher or publishing book: {e}")

    # Создание платформы
    try:
        platform = ShopPlatform()
        platform.add_user(user)
        platform.add_book(book)
        platform.add_order(order)
        platform.add_cart(cart)
        platform.add_review(review)
        platform.add_coupon(coupon)
        platform.add_payment(payment)
        platform.add_publisher(publisher)
    except (ValueError, TypeError) as e:
        print(f"Error while adding items to ShopPlatform: {e}")

    with open("platform.json", "w", encoding="utf-8") as out_file:
        json.dump(platform.to_json(), out_file, ensure_ascii=False, indent=4)


    with open("platform.json", "r", encoding="utf-8") as inp_file:
        data = json.load(inp_file)
        loaded_platform = ShopPlatform.from_json(data)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
