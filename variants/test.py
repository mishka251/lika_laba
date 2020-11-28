from data_classes import InputData


def f(x: float) -> float:
    return (x-4)*(x-4)


def df_dx(x: float) -> float:
    return 2*x


[a, b] = (3, 5)
n = 11

input_data = InputData(2, f, n, (a, b), df_dx, '(x-4)^2')
