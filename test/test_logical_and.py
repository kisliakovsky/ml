from unittest import TestCase

from src.core import LogicalAnd


class TestLogicalAnd(TestCase):
    def test_both_true(self):
        a = LogicalAnd(True, True)
        self.assertTrue(a.boolean_value())

    def test_one_true_one_false(self):
        a = LogicalAnd(True, False)
        self.assertFalse(a.boolean_value())
