
class CalculateTotalCheckoutValue(object):
    """ Calculates the total checkout value
    Attributes:
        input_values(list(str)): list containing all the items to be purchased.
        supermarket(<SuperMarket>): supermarket info necessary to calculate the total checkout value.
    """
    def __init__(self, input_values, supermarket):
        self.input_values = input_values
        self.supermarket = supermarket

    def call(self):
        total_checkout_value = 0

        for input_value in self.input_values:
            if len(input_value) == 1:
                total_checkout_value += self._get_single_item_price(input_value)
            elif len(input_value) == 2:
                quantity = int(input_value[0])
                total_checkout_value += self._get_multiple_item_price(input_value[1], quantity)

        return total_checkout_value

    def _get_single_item_price(self, item_name):
        """ Fetches the item_price for an item that's only being bought once.
        :param item_name: name of item to search for.
        :type item_name: str
        :return: price to pay.
        """
        stock_keeping_unit = self.supermarket.get_stock_keeping_unit(item_name)

        if stock_keeping_unit:
            return stock_keeping_unit.price
        return 0

    def _get_multiple_item_price(self, item_name, quantity):
        """ Fetches the item_price for an item thats being bought multiple times.
        :param item_name: name of item to search for.
        :type item_name: str
        :param quantity: quantity of item to buy.
        :type quantity: int
        :return: price to pay.
        """
        stock_keeping_unit = self.supermarket.get_stock_keeping_unit(item_name)

        if stock_keeping_unit:
            if quantity in stock_keeping_unit.special_offers:
                return stock_keeping_unit.special_offers[quantity]
            return stock_keeping_unit.price * quantity
        return 0

