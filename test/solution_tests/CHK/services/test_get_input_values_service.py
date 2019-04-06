from lib.solutions.CHK.services.get_input_values_service import GetInpuValuesService


class TestGetInputValuesService:
    def test_get_input_values_with_valid_input(self):
        valid_input = 'A, 2A, 3B, C, D,'
        expected_return_value = ['A', '2A', '3B', 'C', 'D']

        service = GetInpuValuesService(valid_input)
        returned_value = service.call()

        assert expected_return_value == returned_value

    def test_get_input_values_with_invalid_input(self):
        valid_input = '123 123 31312'
        expected_return_value = -1

        service = GetInpuValuesService(valid_input)
        returned_value = service.call()

        assert expected_return_value == returned_value

