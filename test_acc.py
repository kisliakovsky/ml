from unittest import TestCase

from main import Acc


class TestAcc(TestCase):

    def test_float_value(self):
        acc = Acc([1, 0, 1, 0, 0], [1, 1, 1, 0, 0])
        self.assertEqual(acc.float_value(), 0.8)
