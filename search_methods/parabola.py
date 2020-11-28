from data_classes import InputData, CalculationResult
from search_methods.base import SearchMethod


class ParabolMethod(SearchMethod):
    method_name = 'Метод парабол'

    # TODO fix
    def __call__(self, data: InputData) -> CalculationResult:
        (a, b) = data.interval

        c = (a + b) / 2

        y_a = data.function(a)
        y_b = data.function(b)
        y_c = data.function(c)

        for _ in range(data.n):
            t = c + 0.5 * ((b - c) * (b - c) * y_a - y_c - (c - a) * (c - a) * (y_b - y_c)) / (
                        (b - c) * (y_a - y_c) + (c - a) * (y_b - y_c))

            x = t if t != c else (a + c) / 2
            y = data.function(x)

            if x < c:
                if y < y_c:
                    b = c
                    c = x
                    y_b = y_c
                    y_c = y
                elif y == y_c:
                    a = x
                    b = c
                    c = (x + c) / 2
                    y_a = y
                    y_b = y_c
                    y_c = data.function(c)

                else:
                    a = x
                    y_a = y
            else:
                if y < y_c:
                    a = c
                    c = x
                    y_a = y_c
                    y_c = y
                elif y == y_c:
                    a = c
                    b = x
                    c = (x + c) / 2
                    y_a = y_c
                    y_b = y
                    y_c = data.function(c)

                else:
                    b = x
                    y_b = y

        return CalculationResult(self.method_name, (a, b), x, y, b - a)
