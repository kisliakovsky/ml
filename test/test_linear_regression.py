from unittest import TestCase

from src.model import LinearRegression, ParametersGenerator


class TestLinearRegression(TestCase):

    def test_apply(self):
        parameters = next(iter(ParametersGenerator(min_value=1, max_value=10, step=1, number_of_parameters=4)))
        regression = LinearRegression(parameters[1:], parameters[0])
        self.assertEqual(regression.rational_value([2, 10, 1]), 14)
        regression = LinearRegression([16, 0, -10], 20)
        self.assertEqual(regression.rational_value([2, 10, 1]), 42)
