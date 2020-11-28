from abc import ABC

from data_classes import InputData, CalculationResult


class SearchMethod(ABC):
    method_name: str

    def __call__(self, data: InputData) -> CalculationResult:
        pass
