from lib.solutions.CHK.models.supermarket import SuperMarket
from lib.solutions.CHK.models.stock_keeping_unit import StockKeepUnit
from lib.solutions.CHK.handlers.checkout_handler import CheckoutHandler


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    # create start stock keeping_units
    item_a = StockKeepUnit('A', 50, {3: 130})
    item_b = StockKeepUnit('B', 30, {2: 45})
    item_c = StockKeepUnit('C', 20, {})
    item_d = StockKeepUnit('D', 15, {})

    # create supermarket
    supermarket = SuperMarket()
    supermarket.add_several_stock_keeping_units([item_a, item_b, item_c, item_d])

    raise NotImplementedError()

