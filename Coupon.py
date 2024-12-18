class Coupon:
    def __init__(self, code: str, discount: float):
        if not isinstance(code, str):
            raise TypeError("Coupon code must be a string.")
        if not isinstance(discount, (float, int)) or not (0 < discount <= 100):
            raise ValueError("Discount must be a number between 0 and 100")
        self.code = code
        self.__discount = discount
        self.__is_active = True

    def to_json(self) -> dict:
        return {
            "code": self.code,
            "discount": self.__discount,
            "is_active": self.__is_active,
        }

    @classmethod
    def from_json(cls, data: dict):
        coupon = cls(code=data["code"], discount=data["discount"])
        coupon.__is_active = data["is_active"]
        return coupon

    def apply(self, total: float):
        if not isinstance(total, (float, int)) or total < 0:
            raise ValueError("Total must be a positive number")
        if not self.__is_active:
            raise ValueError("Coupon is not active")
        return total * (1 - self.__discount / 100)

    def deactivate(self):
        self.__is_active = False


