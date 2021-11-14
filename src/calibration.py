from typing import List

from src.accuracy import Mse
from src.model import ParametersGenerator, LinearRegression


class Calibration(object):
    def __init__(self, features: List[List[int]], real: List[int]):
        self.__features = features
        self.__real = real

    def __mses_and_parameters(self, min_value: int, max_value: int, step: int, number_of_parameters: int):
        for parameters in ParametersGenerator(
                min_value=min_value,
                max_value=max_value,
                step=step,
                number_of_parameters=number_of_parameters
        ):
            regression = LinearRegression(parameters)
            predicted = list(map(regression.apply, self.__features))
            yield Mse(self.__real, predicted).rational_value(), parameters

    def run(self, min_value: int, max_value: int, step: int, number_of_parameters: int):
        mses_and_parameters = list(zip(*self.__mses_and_parameters(min_value, max_value, step, number_of_parameters)))
        mses = list(mses_and_parameters[0])
        parameters = mses_and_parameters[1]
        return parameters[mses.index(min(mses))]
