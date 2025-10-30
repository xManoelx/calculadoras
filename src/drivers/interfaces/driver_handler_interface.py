from abc import ABC, abstractmethod
from typing import List

# Classe que define a interface para manipuladores de drivers
class DriverHandlerInterface(ABC):
    
    @abstractmethod # Decorador que indica que o método é abstrato
    # Método abstrato que deve ser implementado por subclasses
    def standard_derivation(self, numbers: list[float]) -> float:
        """Calculate the standard deviation of a list of numbers."""
        pass

    @abstractmethod
    # Funcao para calcular a variancia usando numpy
    def variance(self, numbers: List[float]) -> float:
        """Calculate the variance of a list of numbers."""
        pass