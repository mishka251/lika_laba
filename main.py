from math import exp
from dataclasses import dataclass
from typing import Tuple, Callable, List
from abc import ABC


@dataclass()
class InputData:
    variant: int
    function: Callable[[float], float]
    n: int
    interval: Tuple[float, float]
    df_dx: Callable[[float], float] = None
    str_function: str = None


@dataclass()
class CalculationResult:
    method_name: str
    interval: Tuple[float, float]
    min_point: float
    min_value: float
    interval_length: float


class SearchMethod(ABC):
    method_name: str

    def __call__(self, data: InputData) -> CalculationResult:
        pass


class PassiveBlockSearch(SearchMethod):
    method_name = 'Алгоритм пассивного поиска минимума'

    def __call__(self, data: InputData) -> CalculationResult:
        (a, b) = data.interval
        delta = (b - a) / data.n
        if data.n % 2 == 0:  # четное
            k = data.n // 2
            step = (b - a) / (k + 1)
            x2i = [a + i * step for i in range(1, data.n)]
            x2i_1 = [x - delta for x in x2i]
            points = []
            for x_2i, x_2i1 in zip(x2i, x2i_1):
                points.append(x2i_1)
                points.append(x_2i)
        else:  # нечетное
            step = (b - a) / (data.n + 1)
            points = [a + i * step for i in range(1, data.n)]

        min_index, minimum = min(enumerate(points), key=lambda t: data.function(t[1]))
        left = points[min_index - 1]
        right = points[min_index + 1]
        eps = 2 * step if data.n % 2 == 1 else step + delta
        return CalculationResult(self.method_name, (left, right), minimum, data.function(minimum), eps)


class BlockSearch(SearchMethod):
    method_name = 'Алгоритм равномерного блочного поиска'

    def __call__(self, data: InputData) -> CalculationResult:
        (a, b) = data.interval
        x_k = (a + b) / 2

        for _ in range(data.n):
            step = (b - a) / (data.n + 1)
            points = [a + i * step for i in range(1, data.n)]
            min_index, minimum = min(enumerate(points), key=lambda t: data.function(t[1]))

            a = points[min_index - 1]
            b = points[min_index + 1]

            x_k = minimum

        return CalculationResult(self.method_name, (a, b), x_k, data.function(x_k), (b - a) / 2)


class BinarySearch(SearchMethod):
    method_name = 'Алгоритм деления интервала пополам'

    def __call__(self, data: InputData) -> CalculationResult:
        (a, b) = data.interval
        x_2 = (b - a) / 2
        for _ in range(data.n):
            x_1 = a + (a + x_2) / 2
            x_3 = (x_2 + b) / 2

            points = [a, x_1, x_2, x_3, b]

            min_index, minimum = min(enumerate(points), key=lambda t: data.function(t[1]))

            a = points[min_index - 1]
            b = points[min_index + 1]

            x_2 = minimum

        return CalculationResult(self.method_name, (a, b), x_2, data.function(x_2), (b - a) / 2)


class Dihotomy(SearchMethod):
    method_name = 'Метод дихотомии'

    def __call__(self, data: InputData) -> CalculationResult:
        (a, b) = data.interval
        x = (b - a) / 2

        delta = ((b - a) / data.n) / 50

        for _ in range(data.n):
            x_1 = x - delta
            x_2 = x + delta

            y_1 = data.function(x_1)
            y_2 = data.function(x_2)

            if y_1 <= y_2:
                b = x_2
            else:
                a = x_1

            x = (b - a) / 2

        return CalculationResult(self.method_name, (a, b), x, data.function(x), (b - a) / 2)


class GoldenFraction(SearchMethod):
    method_name = 'Метод золотого сечения'

    def __call__(self, data: InputData) -> CalculationResult:
        (a, b) = data.interval
        l = 1.618
        x1 = b - (b - a) / l
        x2 = a + (b - a) / l

        y1 = data.function(x1)
        y2 = data.function(x2)

        for _ in range(data.n):
            if y1 <= y2:
                b = x2
                x2 = x1
                x1 = a + b - x2
                y1 = data.function(x1)
            else:
                a = x1
                x1 = x2
                y1 = y2
                x2 = a + b - x1
                y2 = data.function(x2)
        if y1 < y2:
            x = x1
            y = y1
        else:
            x = x2
            y = y2
        return CalculationResult(self.method_name, (x1, x2), x, y, x2 - x1)


class Fibonachy(SearchMethod):
    method_name = 'Метод чисел Фибоначчи'

    def fibs(self, n) -> List[int]:
        fibs = [1, 1]
        for _ in range(2, n+1):
            fibs.append(fibs[-1] + fibs[-2])
        return fibs

    def __call__(self, data: InputData) -> CalculationResult:
        fibs = self.fibs(data.n)
        (a, b) = data.interval

        x1 = a + (b - a) * fibs[data.n - 2] / fibs[data.n]
        x2 = a + (b - a) * fibs[data.n - 1] / fibs[data.n]

        y1 = data.function(x1)
        y2 = data.function(x2)

        for _ in range(data.n - 2):
            if y1 <= y2:
                b = x2
                x2 = x1
                y2 = y1
                x1 = a + b - x2
                y1 = data.function(x1)
            else:
                a = x1
                x1 = x2
                y1 = y2
                x2 = a + b - x1
                y2 = data.function(x2)

        if y1 < y2:
            x = x1
            y = y1
        else:
            x = x2
            y = y2

        return CalculationResult(self.method_name, (x1, x2), x, y, x2 - x1)


class TangentMethod(SearchMethod):
    method_name = 'Метод касательных'

    def __call__(self, data: InputData) -> CalculationResult:
        (a, b) = data.interval
        y1 = data.function(a)
        y2 = data.function(b)

        z1 = data.df_dx(a)
        z2 = data.df_dx(b)
        c = ((b * z2 - a * z1) - (y2 - y1)) / (z2 - z1)
        y = data.function(c)

        for _ in range(data.n):

            z = data.df_dx(c)

            if z == 0:
                return CalculationResult(self.method_name, (c, c), c, y, 0)

            if z < 0:
                a = c
                y1 = y
                z1 = z
            else:
                b = c
                y2 = y
                z2 = z

            c = ((b * z2 - a * z1) - (y2 - y1)) / (z2 - z1)
            y = data.function(c)

        return CalculationResult(self.method_name, (a, b), c, y, b - a)


class ParabolMethod(SearchMethod):
    method_name = 'Метод парабол'

    def __call__(self, data: InputData) -> CalculationResult:
        (a, b) = data.interval

        c = (a+b)/2

        y_a = data.function(a)
        y_b = data.function(b)
        y_c = data.function(c)

        for _ in range(data.n):
            t = c+0.5*((b-c)*(b-c)*y_a-y_c-(c-a)*(c-a)*(y_b-y_c))/((b-c)*(y_a-y_c)+(c-a)*(y_b-y_c))

            x = t if t != c else (a+c)/2
            y = data.function(x)

            if x<c:
                if y<y_c:
                    b=c
                    c=x
                    y_b=y_c
                    y_c=y
                elif y==y_c:
                    a=x
                    b=c
                    c=(x+c)/2
                    y_a=y
                    y_b=y_c
                    y_c =data.function(c)

                else:
                    a=x
                    y_a=y
            else:
                if y<y_c:
                    a=c
                    c=x
                    y_a=y_c
                    y_c=y
                elif y==y_c:
                    a=c
                    b=x
                    c=(x+c)/2
                    y_a=y_c
                    y_b=y
                    y_c = data.function(c)

                else:
                    b=x
                    y_b=y

        return CalculationResult(self.method_name,(a, b), x, y, b-a)



def f(x: float) -> float:
    return x * x + 4 * exp(-x / 4)

def df_dx(x:float)->float:
    return 2*x-exp(x)

[a, b] = (0, 1)
n = 23

inputData = InputData(2, f, n, (a, b), df_dx)
print(inputData)
methods = [PassiveBlockSearch(), BlockSearch(), BinarySearch(), Dihotomy(), GoldenFraction(), Fibonachy(), TangentMethod(),ParabolMethod()]
for method in methods:
    print(method(inputData))
