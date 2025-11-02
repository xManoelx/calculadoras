from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface
from flask import request as FlaskRequest
from typing import Dict, List

class Calculator3:

    ''' 
    CALCULADORA 3 - CÁLCULO DE VARIÂNCIA E MULTIPLICAÇÃO 
    
    N números são enviados.

    Caso a variancia de todos esses numeros seja menor que a multiplicação dos mesmos,
    é apresentado uma informação de sucesso ao usuário
    
    Caso contrário, é retornado um erro.
    
    ### Utiliza o metodo 'var' da lib numpy para calcular a variancia ###
    '''

    # Função construtora da classe Calculator3
    def __init__(self, driver_handler: DriverHandlerInterface) -> None:
        self.__driver_handler = driver_handler

    # Função que realiza o cálculo específico da Calculator3
    def calculate(self, request: FlaskRequest) -> Dict: # type: ignore
        body = request.json
        input_data = self.__validate_body(body)

        variance = self.__calculate_variance(input_data)
        multiplication = self.__calculate_multiplication(input_data)
        self.__verify_result(variance, multiplication)

        formated_response = self.__format_response(variance)
        return formated_response

    # Funcao para validar o corpo da requisição
    def __validate_body(self, body: Dict) -> list[float]:
        if 'numbers' not in body:
            raise Exception("Body mal formatado: 'numbers' ausente")
        
        input_data = body['numbers']
        return input_data

    # Funcao para calcular a variância dos números fornecidos
    def __calculate_variance(self, numbers: List[float]) -> float:
        variance = self.__driver_handler.variance(numbers)
        return float(variance)
    
    # Funcao para calcular a multiplicacao dos numeros fornecidos
    def __calculate_multiplication(self, numbers: List[float]) -> float:
        multiplication = 1 
        for num in numbers: multiplication *= num
        return multiplication
    
    # Funcao para verificar se o resultado do cálculo é válido
    def __verify_result(self, variance: float, multiplication: float) -> None:
        if variance < multiplication:
            raise Exception("Resultado inválido: variância menor que multiplicação")
        
    # Formatação da resposta
    def __format_response(self, variance: float) -> Dict:
        return {
            "data": {
                "Calculator": 3,
                "variance": round(variance, 2),
                "success": True
            }
        }