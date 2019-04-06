from lib.solutions.HLO import hello_solution


class TestHello:
    def test_hello(self):
        expected_return_value = 'Hello, Miguel!'
        assert hello_solution.hello('Miguel') == expected_return_value
