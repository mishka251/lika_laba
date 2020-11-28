from data_classes import InputData, CalculationResult
from search_methods.base import SearchMethod


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

        for _ in range(data.n-3):

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
