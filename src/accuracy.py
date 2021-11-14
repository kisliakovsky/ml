import math
from functools import reduce
from numbers import Rational
from typing import List

from src.core import RationalMicrotype, Sum, Square


class Mse(RationalMicrotype):
    def __init__(self, real: List[Rational], predicted: List[Rational]):
        self.__real = real
        self.__predicted = predicted
        if len(real) != len(predicted):
            raise ValueError("Number of real and predicted values must be equal")

    def __differences(self):
        for i, y in enumerate(self.__real):
            yield y - self.__predicted[i]

    def rational_value(self) -> Rational:
        return reduce(Sum.sum, map(Square.square, self.__differences())) / len(self.__real)

    def __str__(self):
        return f"{self.rational_value()}"


class Acc(RationalMicrotype):
    def __init__(self, real: List[Rational], predicted: List[Rational], rel_tol: float = 1e-3):
        self.__real = real
        self.__predicted = predicted
        self.__rel_tol = rel_tol
        if len(real) != len(predicted):
            raise ValueError("Number of real and predicted values must be equal")

    def __matches(self):
        for i, y in enumerate(self.__real):
            yield 1 if math.isclose(y, self.__predicted[i], rel_tol=self.__rel_tol) else 0

    def rational_value(self) -> Rational:
        return reduce(Sum.sum, self.__matches()) / len(self.__real)
