from unittest import TestCase

from src.model import Const


class TestConst(TestCase):

    def test_apply(self):
        const = Const(1)
        self.assertEqual(const.apply([1, 2]), 1)
        self.assertEqual(const.apply([3]), 1)
