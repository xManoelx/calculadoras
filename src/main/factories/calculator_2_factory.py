from src.calculators.calculator_2 import Calculator2
from src.drivers.numpy_handler import NumpyHandler

def calculator_2_factory():
    numpy_handler = NumpyHandler()  # Instancia o manipulador de driver Numpy
    calc = Calculator2(numpy_handler)
    return calc