
class CalculateTotalCheckoutValueService:
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
            if not item.special_offers:
                total_checkout_value += item.price * count
            else:
                total_checkout_value += self._get_item_total_checkout_value_from_several_special_offers(item, count)

        return total_checkout_value

    def _get_item_total_checkout_value_from_several_special_offers(self, item, count):
        """ Returns the total checkout value needed to pay for an item that can have several special offers.

        :param item: stock keeping unit present in the supermarket.
        :type item: <StockKeepingUnit>
        :param count: total number of times the item is being bought.
        :type count: int
        :return: total checkout value needed to pay for the `count` of `item`.
        """
        item_total_checkout_value = 0
        item_count = count
        special_offers = item.get_special_offers_sorted_by_item_count()

        for special_offer in special_offers:
            while item_count >= special_offer.count:
                free_item = special_offer.free_item

                if free_item and self._free_item_is_in_checkout_items(free_item):
                    item_total_checkout_value += item.price * special_offer.count
                    item_total_checkout_value -= free_item.price
                if free_item:
                    item_total_checkout_value += item.price * special_offer.count
                else:
                    item_total_checkout_value += special_offer.price
                item_count -= special_offer.count

        return item_total_checkout_value + (item_count * item.price)

    def _free_item_is_in_checkout_items(self, free_item):
        """ Checks if the free item offered in the special offer is part of the checkout items.
        :param free_item: item offered in the special offer.
        :type free_item: <StockKeepingUnit>
        :return: True if it's present in the checkout. False otherwise.
        """
        if free_item.name in self.checkout_items_count:
            return True
        return False
