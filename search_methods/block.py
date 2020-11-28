from math import sqrt

from data_classes import InputData, CalculationResult, BlockSearchResult
from search_methods.base import SearchMethod


class BlockSearch(SearchMethod):
    method_name = 'Алгоритм равномерного блочного поиска'

    def __call__(self, data: InputData) -> CalculationResult:
        (a, b) = data.interval
        x_k = (a + b) / 2

        n, m = 0, 0
        # (N-1) = (n-1)*m
        # n - нечетное, (n-1) - четное
        # N-1 - четное, N д.б. нечетным
        # i == n-1
        for i in range(1, data.n):
            if (data.n-1) % i == 0 and i % 2 == 0:
                n = i+1
                m = (data.n-1) // i

        for _ in range(m):
            step = (b - a) / (n + 1)
            points = [a + i * step for i in range(1, n + 1)]
            min_index, minimum = min(enumerate(points), key=lambda t: data.function(t[1]))

            a = points[min_index - 1] if min_index > 0 else a
            b = points[min_index + 1] if min_index < n - 1 else b

            x_k = minimum

        return BlockSearchResult(self.method_name, (a, b), x_k, data.function(x_k), (b - a) / 2, n, m)
