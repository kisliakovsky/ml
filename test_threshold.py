from unittest import TestCase

from main import Threshold


class TestThreshold(TestCase):

    def test_apply(self):
        threshold = Threshold(120)
        self.assertEqual(threshold.apply([100]), 0)
        self.assertEqual(threshold.apply([290]), 1)
