from flask import Blueprint, jsonify, request

# Nomeia todas as rotas relacionadas a calculadoras
calc_route_bp = Blueprint('calc_routes', __name__) 

# Rota para a calculadora 1
@calc_route_bp.route('/calculator/1', methods=['POST'])
def calculator_1():
    print(request.json)
    return jsonify({"success": True}), 200