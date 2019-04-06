from solutions.CHK.services.get_input_values_service import GetInpuValuesService
from solutions.CHK.services.calculate_total_checkout_value_service import CalculateTotalCheckoutValue


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
        checkout_input_values = GetInpuValuesService(checkout_input).call()

        # invalid input
        for checkout_input_value in checkout_input_values:
            if len(checkout_input_value) > 2:
                return -1

        return CalculateTotalCheckoutValue(checkout_input_values, supermarket).call()


