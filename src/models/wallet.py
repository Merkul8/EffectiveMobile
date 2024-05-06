from models.record import Record


class Wallet:
    """ Условный кошелек который хранит все операции пользователя. """

    def __init__(self, filename):
        self.filename: str = filename
        self.records: list[Record] = self.load_records()

    def load_records(self) -> list[Record]:
        # Загрузка записей
        try:
            with open(self.filename, 'r') as file:
                records = file.readlines()
            return [self.parse_record(record) for record in records]
        except FileNotFoundError:
            return []

    def parse_record(self, record_str: str) -> Record:
        # Чтение конкретной записи
        parts = record_str.split(';')
        date, category, amount, description = [part.split(':')[-1] for part in parts]
        return Record(date, category, float(amount), description)

    def add_record(self, record: str) -> None:
        self.records.append(record)
        self.save_records()

    def save_records(self) -> None:
        with open(self.filename, 'w') as file:
            for record in self.records:
                file.write(str(record))

    def get_balance(self) -> int:
        income = sum(record.amount for record in self.records if record.category == 'income')
        expenses = sum(record.amount for record in self.records if record.category == 'expense')
        return income - expenses

    def search_records(self, category=None, date=None, amount=None) -> list[Record]:
        # Поиск по всем полям(все заполнять не обязательно)
        results = self.records
        if category:
            results = [record for record in results if record.category == category]
        if date:
            results = [record for record in results if record.date == date]
        if amount:
            results = [record for record in results if record.amount == amount]
        return results