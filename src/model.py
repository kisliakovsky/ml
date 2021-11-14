from abc import ABC, abstractmethod
from functools import reduce
from itertools import product
from numbers import Rational
from typing import List

from src.core import Sum


class Model(ABC):

    @abstractmethod
    def rational_value(self, params: List[Rational]) -> Rational:
        pass


class Const(Model):
    def __init__(self, value: Rational):
        self.__value = value

    def rational_value(self, params: List[Rational]) -> Rational:
        return self.__value


class Threshold(Model):
    def __init__(self, value: Rational):
        self.__value = value

    def rational_value(self, params: List[Rational]) -> Rational:
        if len(params) == 0:
            raise ValueError("Number of params must be greater than zero")
        return 0 if params[-1] < self.__value else 1


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
    def __init__(self, parameters: List[Rational], bias: Rational):
        self.__coefficients = parameters
        self.__bias = bias

    def __products(self, features: List[Rational]):
        for i, param in enumerate(self.__coefficients):
            yield param * features[i]

    def rational_value(self, params: List[Rational]) -> Rational:
        if len(params) != len(self.__coefficients):
            raise ValueError("Number of params and values must be the equal")
        return reduce(Sum.sum, self.__products(params), self.__bias)
