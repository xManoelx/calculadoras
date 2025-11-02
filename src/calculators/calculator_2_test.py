from .calculator_2 import Calculator2
from typing import Dict
from src.drivers.numpy_handler import NumpyHandler
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface

# Mock da requisição Flask para testes
class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

# Mock do DriverHandlerInterface para testes
class MockDriverHandler:
    def standard_derivation(self, numbers: list[float]) -> float:
        return 3

# Teste de integração da Calculadora 2 com o NumpyHandler
def test_calculator_2_integration():
    mock_request = MockRequest(body = {'numbers':  [2.12, 4.62, 1.32]}) # Valor de entrada para o teste

    driver = NumpyHandler()  # Instância do manipulador de driver
    calculator_2 = Calculator2(driver)  # Instância da Calculadora 2
    formated_reponse = calculator_2.calculate(mock_request)  # Completar o teste conforme a implementação da Calculadora 2
    # print()
    # print('------------------------------------------------')
    # print(formated_reponse)
    # print('------------------------------------------------')

    assert isinstance(formated_reponse, dict) # Verifica se a resposta é um dicionário
    assert formated_reponse == {'data': {'Calculator': 2, 'result': 0.08}} # Verifica se o resultado está correto


# Teste unitário da Calculadora 2
def test_calculator_2():
    mock_request = MockRequest(body = {'numbers':  [2.12, 4.62, 1.32]}) # Valor de entrada para o teste

    driver = MockDriverHandler()  # Instância do manipulador de driver
    calculator_2 = Calculator2(driver)  # Instância da Calculadora 2
    formated_reponse = calculator_2.calculate(mock_request)  # Completar o teste conforme a implementação da Calculadora 2
    # print()
    # print('------------------------------------------------')
    # print(formated_reponse)
    # print('------------------------------------------------')

    assert isinstance(formated_reponse, dict) # Verifica se a resposta é um dicionário
    assert formated_reponse == {'data': {'Calculator': 2, 'result': 0.33}} # Verifica se o resultado está correto