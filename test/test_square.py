from unittest import TestCase

from src.core import Square


class TestSquare(TestCase):
    def test_rational_value(self):
        s = Square(1.1)
        self.assertAlmostEqual(s.rational_value(), 1.21, delta=0.001)
