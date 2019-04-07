from lib.solutions.CHK.services.calculate_total_checkout_value_service import CalculateTotalCheckoutValue
from lib.solutions.CHK.models.stock_keeping_unit import StockKeepUnit
from lib.solutions.CHK.models.supermarket import SuperMarket


class TestCalculateTotalCheckoutValueService:
    def __init__(self):
        special_offer_item_a = SpecialOffer(3, 130)
        special_offer_item_b = SpecialOffer(2, 45)
        item_a = StockKeepUnit('A', 50, special_offer_item_a)
        item_b = StockKeepUnit('B', 30, special_offer_item_b)
        item_c = StockKeepUnit('C', 20, {})
        item_d = StockKeepUnit('D', 15, {})

        self.mock_supermarket = SuperMarket([item_a, item_b, item_c, item_d])

    def test_calculate_total_checkout_value_service_with_same_items_count(self):
        """ Tests calculating the checkout value with single quantity items.

        For the provided mock values should return:
            50+30+20+15 = 115
        """
        input_items_count = {'A': 1, 'B': 1, 'C': 1, 'D': 1}
        expected_value = 115

        service = CalculateTotalCheckoutValue(input_items_count, self.mock_supermarket)
        returned_value = service.call()

        assert returned_value, expected_value

    def test_calculate_total_checkout_value_service_with_different_items_count(self):
        """ Tests calculating the checkout value with single and multiple quantity items.

        For the provided mock values should return:
            130 + 30 + 40 + 20 = 220
        """
        input_items_count = {'A': 3, 'B': 2, 'C': 1, 'D': 1}
        expected_value = 220

        service = CalculateTotalCheckoutValue(input_items_count, self.mock_supermarket)
        returned_value = service.call()

        assert returned_value, expected_value


