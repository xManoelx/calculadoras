from flask import Flask, jsonify
from src.main.routes.calculators import calc_route_bp


app = Flask(__name__) # Cria a aplicação Flask
app.register_blueprint(calc_route_bp) # Registra o Blueprint das rotas de calculadoras