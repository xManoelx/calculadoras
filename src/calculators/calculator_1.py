# impotando o módulo request e renomeando-o para evitar conflitos
from flask import Request as FlaskRequest
from typing import Dict

# Definindo a classe Calculator1
class Calculator1:

    '''
     CALCULADORA 1

     Um número é dividido em 3 partes iguais.

     A primeira parte é dividida por 4 e seu resultado é somado a 7. Depois é elevado ao quadrado e multiplicado por 0.257
     A segunda parte é elevada a potência de 2.121, dividida por 5 e somada a 1
     A terceira parte se mantém no mesmo valor

     Por fim, os 3 resultados são somados e retornados.
    '''

    # Método para realizar cálculos
    def calculate(self, request: FlaskRequest) -> Dict:
        body = request.json
        input_data = self.__validate_body(body)

        splited_number = input_data / 3 # Divide o número em 3 partes iguais

        first_process_result = self.__first_process(splited_number)     # Primeiro processo de cálculo
        second_process_result = self.__second_process(splited_number)   # Segundo processo de cálculo
        third_process_result = self.__third_process(splited_number)     # Terceiro processo de cálculo

        calc_result = first_process_result + second_process_result + third_process_result
        response = self.__format_response(calc_result)

        # print('------------------------------------------------')
        # print("Input da Calculadora 1:", input_data)
        # print("Resultado da Calculadora 1:", calc_result)
        # print('------------------------------------------------')

        return response

    # Validação do corpo da requisição
    def __validate_body(self, body: Dict) -> float:
        if 'number' not in body:
            raise Exception("Body mal formatado: 'number' ausente")

        input_data = body['number']
        return input_data
    
    # Primeiro processo de cálculo
    def __first_process(self, first_number: float) -> float:
        result_firstPart = ((first_number / 4) + 7) ** 2 * 0.257
        return result_firstPart

    # Segundo processo de cálculo
    def __second_process(self, second_number: float) -> float:
        result_secondPart = (second_number ** 2.121) / 5 + 1
        return result_secondPart

    # Terceiro processo de cálculo
    def __third_process(self, third_number: float) -> float:
        result_thirdPart = third_number
        return result_thirdPart
    
    # Formatação da resposta
    def __format_response(self, calc_result: float) -> Dict:
        return {
            "data": {
                "Calculator": 1,
                "result": round(calc_result, 2)
            }
        }
    