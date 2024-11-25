from Cart import Order
class Payment:
    def __init__(self, order: Order, payment_method: str):
        if not isinstance(order, Order):
            raise TypeError("Order must be an instance of the Order class")
        if payment_method not in ["credit_card", "spb", "bank_transfer"]:
            raise ValueError("Invalid payment method")
        self.__order = order
        self.__payment_method = payment_method
        self.__payment_status = "pending"

    def to_json(self) -> dict:
        return {
            "order": self.__order.to_json(),
            "payment_method": self.__payment_method,
            "payment_status": self.__payment_status,
        }

    @classmethod
    def from_json(cls, data: dict):
        order = Order.from_json(data["order"])
        payment = cls(order=order, payment_method=data["payment_method"])
        payment.payment_status = data["payment_status"]
        return payment
    def process_payment(self):
        self.__payment_status = "completed"
        print(f"Payment for Order {self.__order.order_id} completed successfully!")

