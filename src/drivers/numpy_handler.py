import numpy
from typing import List

# Classe de cobertura para operações externas com numpy
class NumpyHandler:
    def __init__(self) -> None:
        self.__np = numpy

    def standard_derivation(self, numbers: List[float]) -> float:
        return self.__np.std(numbers)