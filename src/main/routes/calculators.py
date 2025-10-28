from flask import Blueprint, jsonify, request
from src.drivers.numpy_handler import NumpyHandler
from src.calculators.calculator_1 import Calculator1
from src.calculators.calculator_2 import Calculator2

# Nomeia todas as rotas relacionadas a calculadoras
calc_route_bp = Blueprint('calc_routes', __name__) 

# Rota para a calculadora 1
@calc_route_bp.route('/calculator/1', methods=['POST'])
def calculator_1():
    calc = Calculator1()
    response = calc.calculate(request) # Chama o método calculate da classe Calculator1 

    return jsonify(response), 200

# Rota para a calculadora 2
@calc_route_bp.route('/calculator/2', methods=['POST'])
def calculator_2():
    numpy_handler = NumpyHandler()  # Instancia o manipulador de driver Numpy
    calc = Calculator2(numpy_handler)
    response = calc.calculate(request) # Chama o método calculate da classe Calculator2

    return jsonify(response), 200
