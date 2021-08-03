from unittest import TestCase

from api.exceptions.invalid_data import InvalidDataException
from api.service.price_calculator import PriceCalculator
from datetime import datetime

class PriceCalculatorTest(TestCase):

    def test_price_1h(self):
        calculator = PriceCalculator()
        start_date = datetime.strptime("01/01/2021 10:00", "%d/%m/%Y %H:%M")
        end_date = datetime.strptime("01/01/2021 11:00", "%d/%m/%Y %H:%M")
        price = calculator.calculate(start_date=start_date, end_date=end_date)
        self.assertEqual(price, 200.00)

    def test_price_30m(self):
        calculator = PriceCalculator()
        start_date = datetime.strptime("01/01/2021 10:00", "%d/%m/%Y %H:%M")
        end_date = datetime.strptime("01/01/2021 10:30", "%d/%m/%Y %H:%M")
        price = calculator.calculate(start_date=start_date, end_date=end_date)
        self.assertEqual(price, 200.00)

    def test_price_65m(self):
        calculator = PriceCalculator()
        start_date = datetime.strptime("01/01/2021 10:00", "%d/%m/%Y %H:%M")
        end_date = datetime.strptime("01/01/2021 11:05", "%d/%m/%Y %H:%M")
        price = calculator.calculate(start_date=start_date, end_date=end_date)
        self.assertEqual(price, 216.00)

    def test_price_invalid(self):
        calculator = PriceCalculator()
        start_date = datetime.strptime("01/01/2021 23:00", "%d/%m/%Y %H:%M")
        end_date = datetime.strptime("01/01/2021 11:00", "%d/%m/%Y %H:%M")
        self.assertRaises(InvalidDataException, calculator.calculate, start_date=start_date, end_date=end_date)

    def test_price_empty(self):
        calculator = PriceCalculator()
        start_date = None
        end_date = None
        self.assertRaises(InvalidDataException, calculator.calculate, start_date=start_date, end_date=end_date)

