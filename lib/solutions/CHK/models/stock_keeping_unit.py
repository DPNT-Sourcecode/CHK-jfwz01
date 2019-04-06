
class StockKeepUnit(object):
    """ StockKeepUnit contains the info of a supermarket item (price, special offers).

    Attributes:
        name (str): name of the supermarket item.
        price (int): price of the item.
        special_offers (dict): different price if you buy X ammount of items.
                               This dict will be {ammount_to_buy: price}
    """
    def __init__(self, name, price, special_offers):
        self.name = name
        self.price = price
        self.special_offers = special_offers

