from .calculator_2 import Calculator2
from typing import Dict

# Mock da requisição Flask para testes
class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

# Teste para a Calculadora 2
def test_calculator_2_calculate():
    mock_request = MockRequest(body = {'numbers':  [2.12, 4.62, 1.32]}) # Valor de entrada para o teste

    calculator_2 = Calculator2() # Instância da Calculadora 2
    formated_reponse = calculator_2.calculate(mock_request)  # Completar o teste conforme a implementação da Calculadora 2
    # print()
    # print('------------------------------------------------')
    # print(formated_reponse)
    # print('------------------------------------------------')

    assert isinstance(formated_reponse, dict) # Verifica se a resposta é um dicionário
    assert formated_reponse == {'data': {'Calculator': 2, 'result': 0.08}} # Verifica se o resultado está correto