from unittest import TestCase

from main import Mse


class TestMse(TestCase):

    def test_float_value(self):
        mse = Mse([20, 25, 30, 40], [21, 25, 27, 45])
        self.assertEqual(mse.float_value(), 8.75)
