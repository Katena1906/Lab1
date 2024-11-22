
from Users import User
from datetime import datetime
class Subscription:
    def __init__(self, user: User, start_date: str, end_date: str):
        if not isinstance(user, User):
            raise ValueError("User must be a non-empty string.")

        if not isinstance(start_date, str) or not isinstance(end_date, str):
            raise ValueError("Dates must be strings in the format 'YYYY-MM-DD'.")

        try:
            self.start_date = datetime.strptime(start_date, "%Y-%m-%d")
            self.end_date = datetime.strptime(end_date, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Dates must be in the format 'YYYY-MM-DD'.")
        if self.end_date < self.start_date:
            raise ValueError("End date cannot be earlier than start date.")
        self.user = user
        self.start_date = start_date
        self.end_date = end_date

    def to_json(self) -> dict:
        return {
            "user": self.user.to_json(),
            "start_date": self.start_date,
            "end_date": self.end_date,
        }

    @classmethod
    def from_json(cls, data:dict):
        user=User.from_json(data["user"])
        start_date=data["start_date"]
        end_date=data["end_date"]
        return cls(user=user, start_date=start_date, end_date=end_date)
