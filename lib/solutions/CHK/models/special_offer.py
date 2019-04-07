
class SpecialOffer:
    """ Represents a special offer that can be done by a supermarket.

    Attributes:
        count(int): number of items needed to perform the special offer.
        price(int): new price for the count of items.
    """
    def __init__(self, count, price):
        self.count = count
        self.price = price
