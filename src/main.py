from models.record import Record
from models.wallet import Wallet


def main():
    wallet = Wallet('finances.txt')
    while True:
        print("---------------------")
        print("1. Добавить запись")
        print("2. Показать баланс")
        print("3. Поиск записей")
        print("4. Выход")
        choice = input("Выберите действие: ")
        if choice == '1':
            date = input("Дата: ")
            while True:
                category = input("Категория (income/expense): ").lower()
                if category in ['income', 'expense']:
                    break
                else:
                    print("Неверная категория. Пожалуйста, введите 'income' или 'expense'.")
            amount = float(input("Сумма: "))
            description = input("Описание: ")
            wallet.add_record(Record(date, category, amount, description))
        elif choice == '2':
            print("-----------------------")
            print(f"Текущий баланс: {wallet.get_balance()}")
            print("-----------------------")
        elif choice == '3':
            category = input("Категория (опционально): ")
            date = input("Дата (опционально): ")
            amount = input("Сумма (опционально): ")
            results = wallet.search_records(category, date, amount)
            if not results:
                print("Поиск не дал результатов.")
            else:
                for record in results:
                    print(record)
        elif choice == '4':
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()