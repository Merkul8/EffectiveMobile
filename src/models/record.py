from datetime import datetime

class Record:
    """ Создание записей """

    def __init__(self, date, category, amount, description):
        self.date: datetime = date
        self.category: str = category
        self.amount: int = amount
        self.description: str = description

    def __str__(self) -> str:
        return f"Date: {self.date}; Category: {self.category}; Amount: {self.amount}; Description: {self.description}"