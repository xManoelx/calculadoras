from flask import Request as FlaskRequest
from typing import Dict
from src.drivers.numpy_handler import NumpyHandler
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface

class Calculator2:

    ''' 
    CALCULADORA 2 
    
    N números são enviados.

    Todos esses N números são multiplicados por 11 e elevados a potência de 0.95
    Por fim, é retirado o desvio padrão desses resultados e retornado o inverso desse valor (1/result)
    
    ### Utiliza a lib Numpy para calcular o desvio padrão. ###
    '''

    # Função construtora da classe
    def __init__(self, driver_handler: DriverHandlerInterface) -> None:
        self.driver_handler = driver_handler

    # Função principal da calculadora
    def calculate(self, request: FlaskRequest) -> Dict: 
        body = request.json
        #  print()
        #  print('------------------------------------------------')
        #  print(body)
        #  print('------------------------------------------------')
        
        input_data = self.__validate_body(body)
        #  print('------------------------------------------------')
        #  print(input_data)
        #  print('------------------------------------------------')

        calculator_number = self.__process_data(input_data)
        formated_reponse = self.__format_response(calculator_number)
        return formated_reponse

    # Funcao para validar o corpo da requisição
    def __validate_body(self, body: Dict) -> list[float]:
        if 'numbers' not in body:
            raise Exception("Body mal formatado: 'numbers' ausente")
        
        return body['numbers']
    
    # Processamento dos dados
    def __process_data(self, input_data: list[float]) -> float:
        
        first_process_result = [(num * 11) ** 0.95 for num in input_data]
        # print()
        # print('------------------------------------------------')
        # print(first_process_result)
        # print('------------------------------------------------')

        std_deviation = self.driver_handler.standard_derivation(first_process_result)
        # print('------------------------------------------------')
        # print(f'Desvio Padrão: {std_deviation}')
        # print('------------------------------------------------')

        return float(1 / std_deviation)

    # Formatação da resposta
    def __format_response(self, calculated_number: float) -> Dict:
        return {
            "data": {
                "Calculator": 2,
                "result": round(calculated_number, 2)
            }
        }