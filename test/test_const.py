from unittest import TestCase

from src.model import Const


class TestConst(TestCase):

    def test_apply(self):
        const = Const(1)
        self.assertEqual(const.rational_value([1, 2]), 1)
        self.assertEqual(const.rational_value([3]), 1)
