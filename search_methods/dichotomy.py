from data_classes import InputData, CalculationResult
from search_methods.base import SearchMethod


class Dihotomy(SearchMethod):
    method_name = 'Метод дихотомии'

    def __call__(self, data: InputData) -> CalculationResult:
        (a, b) = data.interval
        x = (b + a) / 2

        eps = ((b - a) / data.n)
        delta = eps / 50

        k = data.n//2

        for _ in range(k):
            x_1 = x - delta
            x_2 = x + delta

            y_1 = data.function(x_1)
            y_2 = data.function(x_2)

            if y_1 <= y_2:
                b = x_2
            else:
                a = x_1

            x = (b + a) / 2

        return CalculationResult(self.method_name, (a, b), x, data.function(x), (b - a) / 2)
