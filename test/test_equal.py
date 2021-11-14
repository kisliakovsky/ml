from unittest import TestCase

from src.core import Equal


class TestEqual(TestCase):
    def test_same(self):
        e = Equal(1, 1)
        self.assertTrue(e.boolean_value())

    def test_different(self):
        e = Equal(1, 2)
        self.assertFalse(e.boolean_value())
