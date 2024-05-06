import tempfile
import unittest
from models.record import Record
from models.wallet import Wallet

class TestRecord(unittest.TestCase):
    def test_record_creation(self):
        record = Record("2023-02-02", "income", 1000.0, "Salary")
        self.assertEqual(record.date, "2023-02-02")
        self.assertEqual(record.category, "income")
        self.assertEqual(record.amount, 1000.0)
        self.assertEqual(record.description, "Salary")

    def test_record_str(self):
        record = Record("2023-02-02", "income", 1000.0, "Salary")
        expected_str = "Date: 2023-02-02; Category: income; Amount: 1000.0; Description: Salary"
        self.assertEqual(str(record), expected_str)



class TestWallet(unittest.TestCase):
    def setUp(self):
        self.temp_file = tempfile.NamedTemporaryFile(delete=False)
        self.wallet = Wallet(self.temp_file.name)

    def tearDown(self):
        self.temp_file.close()

    def test_add_record(self):
        record = Record("2023-02-02", "income", 1000.0, "Salary")
        self.wallet.add_record(record)
        self.assertEqual(len(self.wallet.records), 1)

    def test_get_balance(self):
        record1 = Record("2023-02-02", "income", 1000.0, "Salary")
        record2 = Record("2023-02-03", "expense", 500.0, "Rent")
        self.wallet.add_record(record1)
        self.wallet.add_record(record2)
        self.assertEqual(self.wallet.get_balance(), 500.0)


if __name__ == '__main__':
    unittest.main()