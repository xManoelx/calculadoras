from flask import Blueprint, jsonify, request
from src.calculators.calculator_1 import Calculator1

# Nomeia todas as rotas relacionadas a calculadoras
calc_route_bp = Blueprint('calc_routes', __name__) 

# Rota para a calculadora 1
@calc_route_bp.route('/calculator/1', methods=['POST'])
def calculator_1():
    calc = Calculator1()
    calc.calculate(request) # Chama o método calculate da classe Calculator1 

    return jsonify({"success": True}), 200