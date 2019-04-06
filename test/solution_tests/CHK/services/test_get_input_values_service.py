from lib.solutions.CHK.services.get_input_values_service import GetInpuValuesService


class TestGetInputValuesService:
    def test_get_input_values_with_valid_input(self):
        """ Tests the GetInputValuesService when provided with valid input.

        The service should return all the input values in a list.
        Example:
            For a valid input like 'A, 2A, 3B' it should return ['A', '2A', '3B']
        """
        valid_input = 'A2A3BCD,'
        expected_return_value = ['A', '2A', '3B', 'C', 'D']

        service = GetInpuValuesService(valid_input)
        returned_value = service.call()

        assert expected_return_value == returned_value

    def test_get_input_values_with_invalid_input(self):
        """ Tests the GetInputValuesService when provided with invalid input.

        The service should return an empty list.
        """
        invalid_input = '112331312'
        expected_return_value = []

        service = GetInpuValuesService(invalid_input)
        returned_value = service.call()

        assert expected_return_value == returned_value

