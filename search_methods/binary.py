from data_classes import InputData, CalculationResult
from search_methods.base import SearchMethod


class BinarySearch(SearchMethod):
    method_name = 'Алгоритм деления интервала пополам'

    def __call__(self, data: InputData) -> CalculationResult:
        (a, b) = data.interval
        x_2 = (b + a) / 2
        iters = 0

        while (b-a)>2*data.eps:
            x_1 = (a + x_2) / 2
            x_3 = (x_2 + b) / 2

            points = [x_1, x_2, x_3]

            min_index, minimum = min(enumerate(points), key=lambda t: data.function(t[1]))
            iters += 1

            a = points[min_index - 1] if min_index > 0 else a
            b = points[min_index + 1] if min_index < 2 else b

            x_2 = minimum

        return CalculationResult(self.method_name, (a, b), x_2, data.function(x_2), (b - a) / 2, iters)
