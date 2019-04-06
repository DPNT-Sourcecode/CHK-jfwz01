from lib.solutions.CHK.handlers.checkout_handler import CheckoutHandler
from lib.solutions.CHK.models.stock_keeping_unit import StockKeepUnit
from lib.solutions.CHK.models.supermarket import SuperMarket


class TestCheckoutHandler:
    def __init__(self):
        item_a = StockKeepUnit('A', 50, {3: 130})
        item_b = StockKeepUnit('B', 30, {2: 45})
        item_c = StockKeepUnit('C', 20, {})
        item_d = StockKeepUnit('D', 15, {})

        self.mock_supermarket = SuperMarket([item_a, item_b, item_c, item_d])

    def test_calculate_invalid_input(self):
        """ Tests the checkout handler calculate function with invalid input

        For invalid input it should return -1.
        """
        mock_input = '123'
        expected_return_value = -1

        returned_value = CheckoutHandler.calculate(mock_input, self.mock_supermarket)

        assert expected_return_value == returned_value

    def test_calculate_valid_input_single_item(self):
        """ Tests the checkout handler calculate function a single item in the input.

        For the mock input provided it should return 50.
        """
        mock_input = 'A'
        expected_return_value = 50

        returned_value = CheckoutHandler.calculate(mock_input, self.mock_supermarket)

        assert expected_return_value == returned_value

    def test_calculate_valid_input_multiple_items(self):
        """ Tests the checkout handler calculate function a multiple items in the input.

        For the mock input provided it should return 50+45+20=115.
        """
        mock_input = 'A 2B C'
        expected_return_value = 115

        returned_value = CheckoutHandler.calculate(mock_input, self.mock_supermarket)

        assert expected_return_value == returned_value

