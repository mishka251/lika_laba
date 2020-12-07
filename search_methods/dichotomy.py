from data_classes import InputData, CalculationResult
from search_methods.base import SearchMethod


class Dihotomy(SearchMethod):
    method_name = 'Метод дихотомии'

    def __call__(self, data: InputData) -> CalculationResult:
        (a, b) = data.interval
        x = (b + a) / 2

        delta = data.eps / 50
        iters = 0

        while b-a > 2*data.eps:
            x_1 = x - delta
            x_2 = x + delta

            y_1 = data.function(x_1)
            y_2 = data.function(x_2)
            iters+=2

            if y_1 <= y_2:
                b = x_2
            else:
                a = x_1

            x = (b + a) / 2

        return CalculationResult(self.method_name, (a, b), x, data.function(x), (b - a) / 2, iters)
