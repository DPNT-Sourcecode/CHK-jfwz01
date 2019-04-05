from lib.solutions.SUM import sum_solution


class TestSum:
    def test_sum(self):
        assert sum_solution.sum(1, 2) == 3
        assert sum_solution.sum(2, 2) == 4
        assert sum_solution.sum(3, 2) == 5

