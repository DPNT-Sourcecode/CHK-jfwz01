from solutions.CHK.models.supermarket import SuperMarket
from solutions.CHK.models.stock_keeping_unit import StockKeepUnit
from solutions.CHK.models.special_offer import SpecialOffer
from solutions.CHK.handlers.checkout_handler import CheckoutHandler


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    # create start stock keeping_units
    special_offers_item_a = [SpecialOffer(3, 130), SpecialOffer(5, 200)]
    special_offer_item_b = SpecialOffer(2, 45)
    item_a = StockKeepUnit('A', 50, special_offer_item_a)
    item_b = StockKeepUnit('B', 30, special_offer_item_b)
    item_c = StockKeepUnit('C', 20, {})
    item_d = StockKeepUnit('D', 15, {})
    item_d = StockKeepUnit('E', 40, {})

    # create supermarket
    supermarket = SuperMarket([item_a, item_b, item_c, item_d])

    return CheckoutHandler.calculate(skus, supermarket)

