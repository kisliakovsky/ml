from abc import ABC, abstractmethod
from numbers import Number
from typing import List


class Model(ABC):

    @abstractmethod
    def apply(self, params: List[Number]) -> int:
        pass


class Const(Model):
    def __init__(self, value: int):
        self.value = value

    def apply(self, params: List[Number]) -> int:
        return self.value


class Threshold(Model):
    def __init__(self, value: int):
        self.value = value

    def apply(self, params: List[Number]) -> int:
        return 0 if params[-1] < self.value else 1