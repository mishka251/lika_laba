from dataclasses import dataclass
import os
from typing import Tuple, Callable, List


@dataclass()
class InputData:
    variant: int
    function: Callable[[float], float]
    interval: Tuple[float, float]
    df_dx: Callable[[float], float] = None
    str_function: str = None
    n: int = None
    eps:float = None

    def __str__(self):
        return f'Вариант {self.variant}' + os.linesep + f'Функция - {self.str_function}, интервал {self.interval}, eps = {self.eps}'


@dataclass()
class CalculationResult:
    method_name: str
    interval: Tuple[float, float]
    min_point: float
    min_value: float
    interval_length: float
    iters:int=None

    def __str__(self):
        return f'{self.method_name}{os.linesep}x={self.min_point} y={self.min_value} интервал={self.interval}, экспериментов {self.iters}'


@dataclass()
class BlockSearchResult(CalculationResult):
    n: int=None
    m: int=None

    def __str__(self):
        return super().__str__() + f' m={self.m} n= {self.n}'
