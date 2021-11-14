from unittest import TestCase

from src.model import LinearRegression, ParametersGenerator


class TestLinearRegression(TestCase):

    def test_apply(self):
        parameters = next(iter(ParametersGenerator(min_value=1, max_value=10, step=1, number_of_parameters=4)))
        regression = LinearRegression(parameters)
        self.assertEqual(regression.apply([2, 10, 1]), 14)
        regression = LinearRegression([20, 16, 0, -10])
        self.assertEqual(regression.apply([2, 10, 1]), 42)
