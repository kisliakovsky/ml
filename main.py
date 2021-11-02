from functools import reduce
from typing import List


def print_hi(name):
    print(f'Hi, {name}')


class Mse(object):
    def __init__(self, real: List[int], predicted: List[int]):
        self.real = real
        self.predicted = predicted
        if len(real) != len(predicted):
            raise ValueError("Number of real and predicted values must be equal")

    def __differences(self):
        for i, y in enumerate(self.real):
            yield y - self.predicted[i]

    def float_value(self):
        return reduce(lambda a, b: a + b, map(lambda x: x ** 2, self.__differences())) / len(self.real)


class Acc(object):
    def __init__(self, real: List[int], predicted: List[int]):
        self.real = real
        self.predicted = predicted
        if len(real) != len(predicted):
            raise ValueError("Number of real and predicted values must be equal")

    def __matches(self):
        for i, y in enumerate(self.real):
            yield 1 if y == self.predicted[i] else 0

    def float_value(self):
        return reduce(lambda a, b: a + b, self.__matches()) / len(self.real)


if __name__ == '__main__':
    print_hi('PyCharm')