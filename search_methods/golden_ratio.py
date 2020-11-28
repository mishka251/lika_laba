from data_classes import InputData, CalculationResult
from search_methods.base import SearchMethod


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
                y2=y1
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
        return CalculationResult(self.method_name, (a, b), x, y, b - a)
