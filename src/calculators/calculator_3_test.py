from typing import Dict
from pytest import raises
from .calculator_3 import Calculator3

# Mock da requisição Flask para testes
class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

# Mock do DriverHandlerInterface para testes com erro na variancia
class MockDriverHandlerError:
    def variance(self, numbers: list[float]) -> float:
        return 3
    
# Mock do DriverHandlerInterface para testes
class MockDriverHandler:
    def variance(self, numbers: list[float]) -> float:
        return 1000000

# Funcao de teste da Calculadora 3 com erro de variancia
def test_calculator_3_calculate_with_variance_error():
    mock_request = MockRequest({'numbers': [1, 2, 3, 4, 5]})  # Valor de entrada para o teste
   
    calculator3 = Calculator3(MockDriverHandlerError())

    with raises(Exception) as excinfo:
        calculator3.calculate(mock_request)

    assert str(excinfo.value) == "Resultado inválido: variância menor que multiplicação"
    # print()
    # print('------------------------------------------------')
    # print(excinfo.value)
    # print('------------------------------------------------')

# Funcao de teste da Calculadora 3
def test_calculator_3_calculate():
    mock_request = MockRequest({'numbers': [1, 1, 1, 1, 100]})  # Valor de entrada para o teste
   
    calculator3 = Calculator3(MockDriverHandler())
    response = calculator3.calculate(mock_request)

    # print()
    # print('------------------------------------------------')
    # print(response)
    # print('------------------------------------------------')
    
    assert response == {'data': {'Calculator': 3, 'variance': 1000000, 'success': True}}