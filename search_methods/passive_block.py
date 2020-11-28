from data_classes import InputData, CalculationResult
from search_methods.base import SearchMethod


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
                points.append(x_2i1)
                points.append(x_2i)
        else:  # нечетное
            step = (b - a) / (data.n + 1)
            points = [a + i * step for i in range(1, data.n+1)]

        min_index, minimum = min(enumerate(points), key=lambda t: data.function(t[1]))
        left = points[min_index - 1] if min_index > 0 else a
        right = points[min_index + 1] if min_index < data.n - 1 else b
        eps = 2 * step if data.n % 2 == 1 else step + delta
        return CalculationResult(self.method_name, (left, right), minimum, data.function(minimum), eps)
