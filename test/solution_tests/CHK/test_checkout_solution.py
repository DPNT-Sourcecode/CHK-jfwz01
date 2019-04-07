from lib.solutions.CHK.checkout_solution import checkout


class TestCheckoutSolution:
    def test_checkout_invalid_input_only_numbers(self):
        """ Tests if checkout function is returning -1 for input that only has numbers.
        """
        mock_input = '123'
        expected_value = -1
        returned_value = checkout(mock_input)

        assert expected_value == returned_value

    def test_checkout_invalid_input_lowercases(self):
        """ Tests if checkout function is returning -1 when input has lowercase letters.
        """
        mock_input = 'AAAACCCDDDc'
        expected_value = -1
        returned_value = checkout(mock_input)

        assert expected_value == returned_value

    def test_checkout_valid_input(self):
        """ Tests if checkout function is returning the correct value for a valid input
        For '3A B C' it should return 130+30+20=180
        """
        mock_input = 'AAABC'
        expected_value = 180
        returned_value = checkout(mock_input)

        assert expected_value == returned_value
