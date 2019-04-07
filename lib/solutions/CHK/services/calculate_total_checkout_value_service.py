
class CalculateTotalCheckoutValueService(object):
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
            item = self.supermarket.get_stock_keeping_unit(item_name)
            count = self.checkout_items_count[item_name]

            if not item:
                continue
            if not item.special_offer:
                total_checkout_value += item.price * count
            else:
                total_checkout_value += self._get_item_total_value_with_special_offer(item, count)

        return total_checkout_value

    def _get_item_total_value_with_special_offer(self, item, count):
        """ Returns the total value needed to pay for a StockKeepingUnit item that has a special offer.
        :param item: stock keeping unit present in the supermarket.
        :type item: <StockKeepingUnit>
        :param count: total number of times the item is being bought.
        :type count: int
        :return: total value needed to pay for that ammount of item.
        """
        item_total_value = 0
        special_offer = item.special_offer

        while count >= special_offer.count:
            item_total_value += special_offer.price
            count -= special_offer.count

        return item_total_value + (count * item.price)


