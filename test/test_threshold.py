from unittest import TestCase

from src.model import Threshold


class TestThreshold(TestCase):

    def test_apply(self):
        threshold = Threshold(120)
        self.assertEqual(threshold.rational_value([100]), 0)
        self.assertEqual(threshold.rational_value([290]), 1)
