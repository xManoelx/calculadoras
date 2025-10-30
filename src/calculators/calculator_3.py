from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface
from flask import request as FlaskRequest
from typing import Dict

class Calculator3:

    # Função construtora da classe Calculator3
    def __init__(self, driver_handler: DriverHandlerInterface) -> None:
        self.__driver_handler = driver_handler

    # Função que realiza o cálculo específico da Calculator3
    def calculate(self, request: FlaskRequest) -> Dict: # type: ignore
        pass