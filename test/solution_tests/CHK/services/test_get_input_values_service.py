from lib.solutions.CHK.services.get_input_values_service import GetInpuValuesService


class TestGetInputValuesService:
    """ Tests the GetInputValuesService when provided with valid and invalid inputs.

    The service should return all the correct values in a list.
    Example:
        For a valid input like 'A, 2A, 3B' it should return ['A', '2A', '3B']
        For an invalid input like '1, 2, 3, 123' it should return []
    """
    def test_get_input_values_with_valid_input(self):
        valid_input = 'A, 2A, 3B, C, D,'
        expected_return_value = ['A', '2A', '3B', 'C', 'D']

        service = GetInpuValuesService(valid_input)
        returned_value = service.call()

        assert expected_return_value == returned_value

    def test_get_input_values_with_invalid_input(self):
        invalid_input = '1 123 31312'
        expected_return_value = []

        service = GetInpuValuesService(invalid_input)
        returned_value = service.call()

        assert expected_return_value == returned_value


