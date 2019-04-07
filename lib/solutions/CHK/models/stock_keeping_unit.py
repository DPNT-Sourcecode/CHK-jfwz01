
class StockKeepUnit(object):
    """ StockKeepUnit contains the info of a supermarket item (price, special offers).

    Attributes:
        name (str): name of the supermarket item.
        price (int): price of the item.
        special_offer (<SpecialOffer>): different price if you buy X ammount of items.
    """
    def __init__(self, name, price, special_offer):
        self.name = name
        self.price = price
        self.special_offer = special_offer

