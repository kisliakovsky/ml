from unittest import TestCase

from src.calibration import Calibration


class TestCalibration(TestCase):
    def test_run(self):
        calibration = Calibration(
            [[2, 10, 1], [1, 2, 0], [3, 15, 1], [5, 5, 0], [2, 7, 0]],
            [40, 45, 60, 100, 50]
        )
        params = calibration.run(min_value=-10, max_value=20, step=1, number_of_parameters=4)
        self.assertEqual(params, (20, 16, 0, -10))
