
class SuperMarket(object):
    """ SuperMarket contains the info on all the stock_keeping_units present in a supermarket.

    Attributes:
        stock_keeping_units(list(<StockKeepingUnit>): contains information about several supermarket items.
    """
    def __init__(self):
        self.stock_keeping_units = []

    def add_stock_keeping_unit(self, stock_keeping_unit):
        """ Appends a new stock_keeping_unit to the supermark list of stock_keeping_units
        :param stock_keeping_unit: contains info on a supermarket item.
        :type stock_keeping_unit: <StockKeepingUnit>
        """
        self.stock_keeping_units.append(stock_keeping_unit)

    def add_several_stock_keeping_units(self, list_of_stock_keeping_units):
        """ Adds several supermarket items to the supermarket.
        :param list_of_stock_keeping_units: list containing info on several supermarket items.
        :type list_of_stock_keeping_units: list(<StockKeepingUnit>)
        """
        for stock_keeping_unit in list_of_stock_keeping_units:
            self.add_stock_keeping_unit(stock_keeping_unit)

    def get_stock_keeping_unit(self, name):
        """ Searches for a specific stock_keeping_unit by name.
        :param name: name of item to search
        :return: <StockKeepingUnit> or None
        """
        for stock_keeping_unit in self.stock_keeping_units:
            if stock_keeping_unit.name == name:
                return stock_keeping_unit
        return None
