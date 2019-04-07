
class StockKeepUnit:
    """ StockKeepUnit contains the info of a supermarket item (price, special offers).

    Attributes:
        name (str): name of the supermarket item.
        price (int): price of the item.
        special_offers ([<SpecialOffer>]): list of special offers that allows to
                                           buy X ammount of items at a different price.
    """
    def __init__(self, name, price, special_offers):
        self.name = name
        self.price = price
        self.special_offers = special_offers

    def get_special_offers_sorted_by_item_count(self):
        """ Returns the special offers of a StockKeepUnit sorted in descending order of item count.
        :return: List of <SpecialOffer> sorted in descending order of item count.
        """
        return sorted(self.special_offers, key=lambda special_offer: special_offer.count, reverse=True)



