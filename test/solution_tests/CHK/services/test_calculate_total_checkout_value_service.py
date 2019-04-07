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
        special_offers_item_a = [SpecialOffer(3, 130, None), SpecialOffer(5, 200, None)]
        special_offers_item_b = [SpecialOffer(2, 45, None)]
        item_a = StockKeepUnit('A', 50, special_offers_item_a)
        item_b = StockKeepUnit('B', 30, special_offers_item_b)
        item_c = StockKeepUnit('C', 20, [])
        item_d = StockKeepUnit('D', 15, [])
        special_offers_item_e = [SpecialOffer(2, 0, item_b)]
        item_e = StockKeepUnit('E', 40, special_offers_item_e)

        mock_supermarket = SuperMarket([item_a, item_b, item_c, item_d, item_e])
        input_items_count = {'A': 1, 'B': 1, 'C': 1, 'D': 1, 'E': 1}
        expected_value = 155

        service = CalculateTotalCheckoutValueService(input_items_count, mock_supermarket)
        returned_value = service.call()

        assert returned_value, expected_value

    def test_calculate_total_checkout_value_service_with_different_items_count(self):
        """ Tests calculating the checkout value with single and multiple quantity items.

        For the provided mock values should return:
            200+130+50+45+40+20+40 = 505
        """
        special_offers_item_a = [SpecialOffer(3, 130, None), SpecialOffer(5, 200, None)]
        special_offers_item_b = [SpecialOffer(2, 45, None)]
        item_a = StockKeepUnit('A', 50, special_offers_item_a)
        item_b = StockKeepUnit('B', 30, special_offers_item_b)
        item_c = StockKeepUnit('C', 20, [])
        item_d = StockKeepUnit('D', 15, [])
        special_offers_item_e = [SpecialOffer(2, 0, item_b)]
        item_e = StockKeepUnit('E', 40, special_offers_item_e)

        mock_supermarket = SuperMarket([item_a, item_b, item_c, item_d, item_e])
        input_items_count = {'A': 9, 'B': 2, 'C': 1, 'D': 1, 'E': 1}
        expected_value = 505

        service = CalculateTotalCheckoutValueService(input_items_count, mock_supermarket)
        returned_value = service.call()

        assert returned_value, expected_value

    def test_calculate_total_checkout_value_service_with_free_item_special_offer(self):
        """ Tests calculating the checkout value with single and multiple quantity items.

        For the provided mock values should return:
            200+130+50+40+20+80 = 480
        """
        special_offers_item_a = [SpecialOffer(3, 130, None), SpecialOffer(5, 200, None)]
        special_offers_item_b = [SpecialOffer(2, 45, None)]
        item_a = StockKeepUnit('A', 50, special_offers_item_a)
        item_b = StockKeepUnit('B', 30, special_offers_item_b)
        item_c = StockKeepUnit('C', 20, [])
        item_d = StockKeepUnit('D', 15, [])
        special_offers_item_e = [SpecialOffer(2, 0, item_b)]
        item_e = StockKeepUnit('E', 40, special_offers_item_e)

        mock_supermarket = SuperMarket([item_a, item_b, item_c, item_d, item_e])
        input_items_count = {'A': 9, 'B': 1, 'C': 1, 'D': 1, 'E': 2}
        expected_value = 520

        service = CalculateTotalCheckoutValueService(input_items_count, mock_supermarket)
        returned_value = service.call()

        assert returned_value, expected_value


