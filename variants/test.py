from data_classes import InputData


def f(x: float) -> float:
    return (x-4)*(x-4)


def df_dx(x: float) -> float:
    return 2*x-8


[a, b] = (0, 14)
n = 39

input_data = InputData(0, f, n, (a, b), df_dx, '(x-4)^2')
