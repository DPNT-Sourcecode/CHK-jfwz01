import re

from solutions.CHK.services.get_item_count_service import GetItemCountService
from solutions.CHK.services.calculate_total_checkout_value_service import CalculateTotalCheckoutValueService


class CheckoutHandler(object):
    @classmethod
    def calculate(cls, checkout_input, supermarket):
        """ Calculates the total checkout value the client will have to pay.

        :param checkout_input: String that contains the checkout input values
        :type checkout_input: str
        :param supermarket: Contains info about the supermarket where the checkout is being performed
        :type supermarket: <SuperMarket>
        :return: Total checkout value that the client needs to pay. Returns -1 if input is invalid
        """
        # return 0 for empty input
        if checkout_input == '':
            return 0
        # return -1 for invalid input
        if not re.match("^[A-Z]*$", checkout_input):
            return -1

        checkout_items_count = GetItemCountService(checkout_input).call()

        return CalculateTotalCheckoutValueService(checkout_items_count, supermarket).call()
