from unittest import TestCase

from main import Acc, Const, Threshold


class TestAcc(TestCase):

    def test_float_value(self):
        acc = Acc([1, 0, 1, 0, 0], [1, 1, 1, 0, 0])
        self.assertEqual(acc.float_value(), 0.8)

    def test_const_model(self):
        const = Const(0)
        real = [1, 0, 1, 0, 0]
        predicted = [const.apply([]) for _ in range(len(real))]
        acc = Acc(real, predicted)
        self.assertEqual(acc.float_value(), 0.6)

    def test_threshold_model(self):
        threshold = Threshold(306)
        real = [0, 1, 0, 0, 0, 1, 0]
        predicted = [threshold.apply([s]) for s in [100, 90, 60, 290, 250, 350, 305]]
        acc = Acc(real, predicted)
        self.assertAlmostEqual(acc.float_value(), 0.857, delta=0.001)
