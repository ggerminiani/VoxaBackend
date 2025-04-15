from flask import Flask, jsonify
from flask_cors import CORS

from database.db import init_db, test_db_connection
from routes.transcript import transcript_bp
from routes.user import user_bp

app = Flask(__name__)
CORS(app)

# Inicializa conexão banco
init_db(app)

# Registra rotas
app.register_blueprint(transcript_bp, url_prefix='/transcricao')
app.register_blueprint(user_bp, url_prefix='/usuario')


@app.route('/')
def index():
    return jsonify({"mensagem": "Servidor Flask rodando!"})


@app.route('/pingdb', methods=['GET'])
def ping_db():
    sucesso = test_db_connection()
    if sucesso:
        return jsonify({"status": "ok", "mensagem": "Conexão com banco OK!"})
    else:
        return jsonify({"status": "erro", "mensagem": "Falha na conexão com banco!"}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
