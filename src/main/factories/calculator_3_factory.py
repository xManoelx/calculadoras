from src.calculators.calculator_3 import Calculator3
from src.drivers.numpy_handler import NumpyHandler

def calculator_3_factory():
    numpy_handler = NumpyHandler()  # Instancia o manipulador de driver Numpy
    calc = Calculator3(numpy_handler)
    return calc