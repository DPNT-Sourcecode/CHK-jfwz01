
class CalculateTotalCheckoutValue(object):
    """ Calculates the total checkout value
    Attributes:
        checkout_items_count(list(str)): list containing all the items to be purchased.
        supermarket(<SuperMarket>): supermarket info necessary to calculate the total checkout value.
    """
    def __init__(self, checkout_items_count, supermarket):
        self.checkout_items_count = checkout_items_count
        self.supermarket = supermarket

    def call(self):
        total_checkout_value = 0

        for item_name in self.checkout_items_count:
            count = self.checkout_items_count[item]
            item = self.supermarket.get_stock_keeping_unit(item)

            if not item:
                break
            if not item.special_offers:
                total_checkout_value += item.price * count
            else:
                


        return total_checkout_value

    def _total_price_with_special_offer(self, item, count):


