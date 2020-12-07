from math import exp, cos, sin

from data_classes import InputData


def f(x: float) -> float:
    return 10*cos(x)+exp(x)


def df_dx(x: float) -> float:
    return -10*sin(x) + exp(x)


[a, b] = (0, 3)
eps = 5e-4

input_data = InputData(10, f, (a, b), df_dx, eps=eps, str_function='10cos(x)+e^x')
