from math import exp

from data_classes import InputData


def f(x: float) -> float:
    return x * x + 4 * exp(-x / 4)


def df_dx(x: float) -> float:
    return 2 * x - exp(-x/4)


[a, b] = (0, 1)
n = 23

input_data = InputData(2, f, n, (a, b), df_dx, 'x^2+4*e^(-x/4)')
