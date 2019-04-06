from lib.solutions.CHK.services.get_item_count_service import GetItemCountService


class TestGetItemCountService:
    def test_get_item_count_with_a_single_item(self):
        """ Tests the GetInputValuesService when provided with a single item


        The service should return a dict containing the single item
        Example:
            For an input like 'A' it should return {'A': 1}
        """
        valid_input = 'A'
        expected_return_value = {'A': 1}

        service = GetItemCountService(valid_input)
        returned_value = service.call()

        assert expected_return_value == returned_value

    def test_get_item_count_with_multiple_items(self):
        """ Tests the GetInputValuesService when provided with a multiple items input

        The service should return a dict containing the count of each item
        Example:
            For an input like 'AAAABBBBCCCC' it should return {'A': 4, 'B': 4, 'C': 4}
        """
        valid_input = 'AAAABBBBCCCC'
        expected_return_value = {'A': 4, 'B': 4, 'C': 4}

        service = GetItemCountService(valid_input)
        returned_value = service.call()

        assert expected_return_value == returned_value


