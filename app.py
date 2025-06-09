import os

from dotenv import load_dotenv
from flask import Flask, jsonify
from flask_cors import CORS

from database.db import init_db
from routes.transcript import transcript_bp
from routes.user import user_bp

load_dotenv()
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET')

CORS(app)

# Inicializa conexão banco
init_db(app)

# Registra rotas
app.register_blueprint(transcript_bp, url_prefix='/transcricao')
app.register_blueprint(user_bp, url_prefix='/usuario')


@app.route('/')
def index():
    return jsonify({"mensagem": "Servidor Flask rodando!"})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
