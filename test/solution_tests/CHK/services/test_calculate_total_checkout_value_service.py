from lib.solutions.CHK.services.calculate_total_checkout_value_service import CalculateTotalCheckoutValueService
from lib.solutions.CHK.models.stock_keeping_unit import StockKeepUnit
from lib.solutions.CHK.models.special_offer import SpecialOffer
from lib.solutions.CHK.models.supermarket import SuperMarket


class TestCalculateTotalCheckoutValueService:
    def test_calculate_total_checkout_value_service_with_same_items_count(self):
        """ Tests calculating the checkout value with single quantity items.

        For the provided mock values should return:
            50+30+20+15+40 = 155
        """
        special_offers_items_a = [SpecialOffer(3, 130), SpecialOffer(5, 200)]
        special_offers_items_b = [SpecialOffer(2, 45)]
        item_a = StockKeepUnit('A', 50, special_offers_items_a)
        item_b = StockKeepUnit('B', 30, special_offers_items_b)
        item_c = StockKeepUnit('C', 20, {})
        item_d = StockKeepUnit('D', 15, {})
        item_e = StockKeepUnit('E', 40, {})

        mock_supermarket = SuperMarket([item_a, item_b, item_c, item_d, item_e])
        input_items_count = {'A': 1, 'B': 1, 'C': 1, 'D': 1, 'E': 1}
        expected_value = 155

        service = CalculateTotalCheckoutValueService(input_items_count, mock_supermarket)
        returned_value = service.call()

        assert returned_value, expected_value

    def test_calculate_total_checkout_value_service_with_different_items_count(self):
        """ Tests calculating the checkout value with single and multiple quantity items.

        For the provided mock values should return:
            200+130+50+45+40+20 = 505
        """
        special_offers_items_a = [SpecialOffer(3, 130), SpecialOffer(5, 200)]
        special_offers_items_b = [SpecialOffer(2, 45)]
        item_a = StockKeepUnit('A', 50, special_offers_items_a)
        item_b = StockKeepUnit('B', 30, special_offers_items_b)
        item_c = StockKeepUnit('C', 20, {})
        item_d = StockKeepUnit('D', 15, {})
        item_e = StockKeepUnit('E', 40, {})

        mock_supermarket = SuperMarket([item_a, item_b, item_c, item_d, item_e])
        input_items_count = {'A': 9, 'B': 2, 'C': 1, 'D': 1, 'E': 1}
        expected_value = 505

        service = CalculateTotalCheckoutValueService(input_items_count, mock_supermarket)
        returned_value = service.call()

        assert returned_value, expected_value

