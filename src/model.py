from abc import ABC, abstractmethod
from functools import reduce
from itertools import product
from numbers import Rational
from typing import List

from src.core import Sum


class Model(ABC):

    @abstractmethod
    def apply(self, features: List[Rational]) -> Rational:
        pass


class Const(Model):
    def __init__(self, parameter: Rational):
        self.__parameter = parameter

    def apply(self, features: List[Rational]) -> Rational:
        return self.__parameter


class Threshold(Model):
    def __init__(self, parameter: Rational):
        self.__parameter = parameter

    def apply(self, features: List[Rational]) -> Rational:
        if len(features) == 0:
            raise ValueError("Number of params must be greater than zero")
        return 0 if features[-1] < self.__parameter else 1


class ParametersGenerator(object):
    def __init__(self, min_value: int, max_value: int, step: int, number_of_parameters: int):
        self.__step = step
        delta = max_value - min_value
        self.__number_of_steps = delta // step + (2 if delta % step > 0 else 1)
        self.__min_value = min_value
        self.__number_of_parameters = number_of_parameters

    def __iter__(self):
        for x in product(
                map(lambda i: i * self.__step + self.__min_value, range(self.__number_of_steps)),
                repeat=self.__number_of_parameters
        ):
            yield x


class LinearRegression(Model):
    def __init__(self, parameters: List[Rational]):
        self.__feature_parameters = parameters[1:]
        self.__bias = parameters[0]

    def __products(self, features: List[Rational]):
        for i, feature_parameter in enumerate(self.__feature_parameters):
            yield feature_parameter * features[i]

    def apply(self, features: List[Rational]) -> Rational:
        if len(features) != len(self.__feature_parameters):
            raise ValueError("Number of params and values must be the equal")
        return reduce(Sum.sum, self.__products(features), self.__bias)
