from flask import Blueprint, jsonify, request
from src.main.factories.calculator_1_factory import calculator_1_factory
from src.main.factories.calculator_2_factory import calculator_2_factory

# Nomeia todas as rotas relacionadas a calculadoras
calc_route_bp = Blueprint('calc_routes', __name__) 

# Rota para a calculadora 1
@calc_route_bp.route('/calculator/1', methods=['POST'])
def calculator_1():
    calc = calculator_1_factory()
    response = calc.calculate(request) # Chama o método calculate da classe Calculator1 

    return jsonify(response), 200

# Rota para a calculadora 2
@calc_route_bp.route('/calculator/2', methods=['POST'])
def calculator_2():
    calc = calculator_2_factory()
    response = calc.calculate(request) # Chama o método calculate da classe Calculator2

    return jsonify(response), 200
