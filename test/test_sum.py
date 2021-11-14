from unittest import TestCase

from src.core import Sum


class TestSum(TestCase):
    def test_rational_value(self):
        s = Sum(2.2, 3.3)
        self.assertAlmostEqual(s.rational_value(), 5.5, delta=0.001)
