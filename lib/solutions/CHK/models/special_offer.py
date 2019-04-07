
class SpecialOffer:
    """ Represents a special offer that can be done by a supermarket.

    Attributes:
        count(int): number of items needed to perform the special offer.
        price(int): new price for the count of items.
        free_item(<StockKeepingUnit>): the special offer instead of a different price offers a free item.
    """
    def __init__(self, count, price, free_item):
        self.count = count
        self.price = price
        self.free_item = free_item

