from .calculator_1 import Calculator1
from typing import Dict
from pytest import raises

# Mock da requisição Flask para testes
class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

# Teste para a Calculadora 1
def test_calculator_1_calculate():
    mock_request = MockRequest(body = {'number':  1}) # Valor de entrada para o teste

    calculator_1 = Calculator1()
    response = calculator_1.calculate(mock_request)

    # Testa o formato esperado da resposta
    assert 'data' in response
    assert 'Calculator' in response['data']
    assert 'result' in response['data']

    # Testa a assertividade da resposta
    assert response['data']['result'] == 14.25
    assert response['data']['Calculator'] == 1

# Teste para corpo de requisição inválido
def test_calculator_1_invalid_body():
    mock_request = MockRequest(body = {'something':  1}) # teste com corpo inválido
    calculator_1 = Calculator1()

    with raises(Exception) as excinfo:
        calculator_1.calculate(mock_request)

    assert str(excinfo.value) == "Body mal formatado: 'number' ausente"

