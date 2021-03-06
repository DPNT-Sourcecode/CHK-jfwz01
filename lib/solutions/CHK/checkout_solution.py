from solutions.CHK.models.supermarket import SuperMarket
from solutions.CHK.models.stock_keeping_unit import StockKeepUnit
from solutions.CHK.models.special_offer import SpecialOffer
from solutions.CHK.handlers.checkout_handler import CheckoutHandler


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    # create start stock keeping_units
    special_offers_item_a = [SpecialOffer(3, 130, None), SpecialOffer(5, 200, None)]
    special_offers_item_b = [SpecialOffer(2, 45, None)]
    item_a = StockKeepUnit('A', 50, special_offers_item_a)
    item_b = StockKeepUnit('B', 30, special_offers_item_b)
    item_c = StockKeepUnit('C', 20, [])
    item_d = StockKeepUnit('D', 15, [])
    special_offers_item_e = [SpecialOffer(2, 0, item_b)]
    item_e = StockKeepUnit('E', 40, special_offers_item_e)

    # create supermarket
    supermarket = SuperMarket([item_a, item_b, item_c, item_d, item_e])

    return CheckoutHandler.calculate(skus, supermarket)
