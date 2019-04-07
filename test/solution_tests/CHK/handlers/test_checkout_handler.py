from lib.solutions.CHK.handlers.checkout_handler import CheckoutHandler
from lib.solutions.CHK.models.stock_keeping_unit import StockKeepUnit
from lib.solutions.CHK.models.supermarket import SuperMarket


class TestCheckoutHandler:
    def test_calculate_empty_input(self):
        """ Tests the checkout handler calculate function with an empty input

        Since it's empty it should return 0.
        """
        item_a = StockKeepUnit('A', 50, {3: 130})
        item_b = StockKeepUnit('B', 30, {2: 45})
        item_c = StockKeepUnit('C', 20, {})
        item_d = StockKeepUnit('D', 15, {})
        mock_supermarket = SuperMarket([item_a, item_b, item_c, item_d])
        mock_input = ''

        expected_return_value = 0
        returned_value = CheckoutHandler.calculate(mock_input, mock_supermarket)

        assert expected_return_value == returned_value

    def test_calculate_invalid_input_only_numbers(self):
        """ Tests the checkout handler calculate function with only numbers input.

        Since it's invalid it should return -1
        """
        item_a = StockKeepUnit('A', 50, {3: 130})
        item_b = StockKeepUnit('B', 30, {2: 45})
        item_c = StockKeepUnit('C', 20, {})
        item_d = StockKeepUnit('D', 15, {})
        mock_supermarket = SuperMarket([item_a, item_b, item_c, item_d])
        mock_input = '123'

        expected_return_value = -1
        returned_value = CheckoutHandler.calculate(mock_input, mock_supermarket)

        assert expected_return_value == returned_value

    def test_calculate_invalid_input_lowercases(self):
        """ Tests the checkout handler calculate function with lowercase letters.

        Since it's invalid it should return -1.
        """
        item_a = StockKeepUnit('A', 50, {3: 130})
        item_b = StockKeepUnit('B', 30, {2: 45})
        item_c = StockKeepUnit('C', 20, {})
        item_d = StockKeepUnit('D', 15, {})
        mock_supermarket = SuperMarket([item_a, item_b, item_c, item_d])
        mock_input = 'ABCDa'

        expected_return_value = -1
        returned_value = CheckoutHandler.calculate(mock_input, mock_supermarket)

        assert expected_return_value == returned_value

    def test_calculate_valid_input_single_item(self):
        """ Tests the checkout handler calculate function a single item in the input.

        For the mock input provided it should return 50.
        """
        item_a = StockKeepUnit('A', 50, {3: 130})
        item_b = StockKeepUnit('B', 30, {2: 45})
        item_c = StockKeepUnit('C', 20, {})
        item_d = StockKeepUnit('D', 15, {})
        mock_supermarket = SuperMarket([item_a, item_b, item_c, item_d])
        mock_input = 'A'

        expected_return_value = 50
        returned_value = CheckoutHandler.calculate(mock_input, mock_supermarket)

        assert expected_return_value == returned_value

    def test_calculate_valid_input_multiple_items(self):
        """ Tests the checkout handler calculate function a multiple items in the input.

        For the mock input provided it should return 130+45+20=195.
        """
        item_a = StockKeepUnit('A', 50, {3: 130})
        item_b = StockKeepUnit('B', 30, {2: 45})
        item_c = StockKeepUnit('C', 20, {})
        item_d = StockKeepUnit('D', 15, {})
        mock_supermarket = SuperMarket([item_a, item_b, item_c, item_d])
        mock_input = 'AAABBC'

        expected_return_value = 115
        returned_value = CheckoutHandler.calculate(mock_input, mock_supermarket)

        assert expected_return_value == returned_value
