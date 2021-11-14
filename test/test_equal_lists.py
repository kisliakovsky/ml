from unittest import TestCase

from src.core import Equal, EqualLists


class TestEqualLists(TestCase):
    def test_same(self):
        e = EqualLists([0, 1, 2, 3, 4], [0, 1, 2, 3, 4])
        self.assertTrue(e.boolean_value())

    def test_almost_same(self):
        e = EqualLists([0, 1, 2, 3, 4], [0, 1, 2, 3, 5])
        self.assertFalse(e.boolean_value())

    def test_different(self):
        e = EqualLists([0, 1, 2, 3, 4], [5, 6, 7, 8, 9])
        self.assertFalse(e.boolean_value())
