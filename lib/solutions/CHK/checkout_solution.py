from solutions.CHK.models.supermarket import SuperMarket
from solutions.CHK.models.stock_keeping_unit import StockKeepUnit
from solutions.CHK.handlers.checkout_handler import CheckoutHandler


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    # create start stock keeping_units
    item_a = StockKeepUnit('A', 50, {3: 130})
    item_b = StockKeepUnit('B', 30, {2: 45})
    item_c = StockKeepUnit('C', 20, {})
    item_d = StockKeepUnit('D', 15, {})

    # create supermarket
    supermarket = SuperMarket([item_a, item_b, item_c, item_d])

    return CheckoutHandler.calculate(skus, supermarket)
