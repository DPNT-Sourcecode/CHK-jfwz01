from lib.solutions.CHK.checkout_solution import checkout


class TestCheckoutSolution:
    def test_checkout_invalid_input(self):
        """ Tests if checkout function is returning -1 for invalid input.
        """
        mock_input = '123'
        expected_value = -1
        returned_value = checkout(mock_input)

        assert expected_value == returned_value

    def test_checkout_valid_input(self):
        """ Tests if checkout function is returning the correct value for a valid input
        For '3A B C' it should return 130+30+20=180
        """
        mock_input = '3A B C'
        expected_value = 180
        returned_value = checkout(mock_input)

        assert expected_value == returned_value

