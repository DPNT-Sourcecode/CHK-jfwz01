from unittest import TestCase
from lib.solutions.CHK.services.calculate_total_checkout_value_service import CalculateTotalCheckoutValue
from lib.solutions.CHK.models.stock_keeping_unit import StockKeepUnit
from lib.solutions.CHK.models.supermarket import SuperMarket


class TestCalculateTotalCheckoutValueService(TestCase):
    def setUp(self):
        item_a = StockKeepUnit('A', 50, {3: 130})
        item_b = StockKeepUnit('B', 30, {2: 45})
        item_c = StockKeepUnit('C', 20, {})
        item_d = StockKeepUnit('D', 15, {})

        self.mock_input_values_all_multiple = ['2A', '2B', '2C', '2C']
        self.mock_supermarket = SuperMarket([item_a, item_b, item_c, item_d])

    def test_with_input_values_all_single(self):
        input_values = ['A', 'B', 'C', 'D']
        # 50+30+20+15
        expected_value = 115

        service = CalculateTotalCheckoutValue(input_values, self.mock_supermarket)
        returned_value = service.call()

        self.assertEqual(returned_value, expected_value)

    def test_with_input_values_single_and_multiple(self):
        input_values = ['3A', 'B', '2C', 'C']
        # 130 + 30 + 40 + 20
        expected_value = 220

        service = CalculateTotalCheckoutValue(input_values, self.mock_supermarket)
        returned_value = service.call()

        self.assertEqual(returned_value, expected_value)

    def test_with_input_values_all_multiple(self):
        input_values = ['3A', '2B', '2C', '2C', '2D']
        # 130 + 45 + 40 + 30
        expected_value = 245

        service = CalculateTotalCheckoutValue(input_values, self.mock_supermarket)
        returned_value = service.call()

        self.assertEqual(returned_value, expected_value)

