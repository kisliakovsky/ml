from unittest import TestCase

from src.model import ParametersGenerator


class TestParametersGenerator(TestCase):

    def test_parameters(self):
        parameters_list = list(ParametersGenerator(min_value=-100, max_value=100, step=10, number_of_parameters=3))
        self.assertEqual(parameters_list[0], (-100, -100, -100))
        self.assertEqual(parameters_list[-1], (100, 100, 100))
