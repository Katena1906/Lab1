from Cart import Order
class Payment:
    def __init__(self, order: Order, payment_method: str):
        if not isinstance(order, Order):
            raise TypeError("Order must be an instance of the Order class")
        if payment_method not in ["credit_card", "spb", "bank_transfer"]:
            raise ValueError("Invalid payment method")
        self.order = order
        self.payment_method = payment_method
        self.payment_status = "pending"

    def to_json(self) -> dict:
        return {
            "order": self.order.to_json(),
            "payment_method": self.payment_method,
            "payment_status": self.payment_status,
        }

    @classmethod
    def from_json(cls, data: dict):
        order = Order.from_json(data["order"])
        payment = cls(order=order, payment_method=data["payment_method"])
        payment.payment_status = data["payment_status"]
        return payment
    def process_payment(self):
        self.payment_status = "completed"
        print(f"Payment for Order {self.order.order_id} completed successfully!")

