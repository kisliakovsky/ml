from abc import ABC, abstractmethod
from functools import reduce
from numbers import Rational
from typing import List


class RationalMicrotype(ABC):

    @abstractmethod
    def rational_value(self) -> Rational:
        pass


class BooleanMicrotype(ABC):

    @abstractmethod
    def boolean_value(self) -> bool:
        pass


class Sum(RationalMicrotype):
    def __init__(self, a: Rational, b: Rational):
        self.__a = a
        self.__b = b

    def rational_value(self) -> Rational:
        return self.__a + self.__b

    @staticmethod
    def sum(a: Rational, b: Rational) -> Rational:
        return Sum(a, b).rational_value()


class Square(RationalMicrotype):

    def __init__(self, a: Rational):
        self.__a = a

    def rational_value(self) -> Rational:
        return self.__a ** 2

    @staticmethod
    def square(a: Rational) -> Rational:
        return Square(a).rational_value()


class LogicalAnd(BooleanMicrotype):

    def __init__(self, a: bool, b: bool):
        self.__a = a
        self.__b = b

    def boolean_value(self) -> bool:
        return self.__a and self.__b

    @staticmethod
    def logical_and(a: bool, b: bool) -> bool:
        return LogicalAnd(a, b).boolean_value()


class Equal(BooleanMicrotype):

    def __init__(self, a: int, b: int):
        self.__a = a
        self.__b = b

    def boolean_value(self) -> bool:
        return self.__a == self.__b

    @staticmethod
    def equal(a: int, b: int) -> int:
        return Equal(a, b).boolean_value()


class EqualLists(BooleanMicrotype):

    def __init__(self, a: List[int], b: List[int]):
        self.__a = a
        self.__b = b

    def boolean_value(self) -> bool:
        return reduce(LogicalAnd.logical_and, map(Equal.equal, self.__a, self.__b), True)

    @staticmethod
    def equal_lists(a: List[int], b: List[int]) -> bool:
        return EqualLists(a, b).boolean_value()
