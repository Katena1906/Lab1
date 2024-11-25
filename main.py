

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
from Subscription import Subscription
from CRUD import CRUD
import json

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    author=None
    try:
        author = Author("Sui", "Ishida")
    except (ValueError, TypeError) as e:
        print(f"Error while creating Author: {e}")

    book=None
    try:
        book = Book("Tokyo Ghoul", 123456, 12.99, "Psychology drama", author)
    except (TypeError, ValueError) as e:
        print(f"Error while creating Book: {e}")

    user=None
    try:
        user = User("Vovchik", "VovchikPomidorchik@mail.com")
    except (ValueError, TypeError) as e:
        print(f"Error while creating User: {e}")

    subscription=None
    try:
        subscription = Subscription(user, "19.06.2024","23.07.2025")
    except (ValueError, TypeError) as e:
        print(f"Error while creating Subscription: {e}")

    review=None
    try:
        review = Review(user, book, "Great book!", 5)
    except (ValueError, TypeError) as e:
        print(f"Error while creating Review: {e}")

    coupon=None
    try:
        coupon = Coupon("ee3he38", 20.99)
    except (TypeError, ValueError) as e:
        print(f"Error while creating Coupon: {e}")

    cart=None
    try:
        cart = Cart(user)
        cart.add_book(book)
    except (TypeError, ValueError) as e:
        print(f"Error while creating Cart or adding book: {e}")

    order=None
    try:
        order = Order("order123", user)
        order.add_book_to_order(book)
    except (TypeError, ValueError) as e:
        print(f"Error while creating Order or adding book to order: {e}")

    payment=None
    try:
        payment = Payment(order, "spb")
    except (TypeError, ValueError) as e:
        print(f"Error while creating Payment: {e}")

    publisher=None
    try:
        publisher = Publisher("Weekly Shonen Jump")
        publisher.publish_book(book)
    except (ValueError, TypeError) as e:
        print(f"Error while creating Publisher or publishing book: {e}")


    platform=None
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


    author2 = Author("Аlexandr", "Elkin")
    book_crud = CRUD(Book)
    book1 = Book("MatAnalyse", 9780747532699, 20.99, "science", author2)
    book2 = Book("Diffurs", 9780451524935, 15.99, "science", author2)
    book_crud.create(book1)
    book_crud.create(book2)
    print(book_crud.read(0).title)

    book_crud.delete(0)

    for book in book_crud.list():
        print(book.title)

    coupon_crud = CRUD(Coupon)

    coupon1 = Coupon("SUMMER21", 20)
    coupon2 = Coupon("WINTER21", 15)

    coupon_crud.create(coupon1)
    coupon_crud.create(coupon2)

    print(coupon_crud.read(0).code)

    coupon_crud.update(1, Coupon("SPRING21", 10))
    coupon_crud.delete(0)

    for coupon in coupon_crud.list():
        print(coupon.code)

