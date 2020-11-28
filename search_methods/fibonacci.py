from data_classes import InputData, CalculationResult
from search_methods.base import SearchMethod
from typing import List


class Fibonachy(SearchMethod):
    method_name = 'Метод чисел Фибоначчи'

    def fibs(self, n) -> List[int]:
        fibs = [1, 1]
        for _ in range(2, n + 1):
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
