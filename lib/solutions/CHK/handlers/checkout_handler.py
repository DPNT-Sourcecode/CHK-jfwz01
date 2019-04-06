from lib.solutions.CHK.services.get_input_values_service import GetInpuValuesService


class CheckoutHandler(object):
    @classmethod
    def checkout(cls, input, supermarket):
        input_values = GetInpuValuesService(input).call()
