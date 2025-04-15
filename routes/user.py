from flask import Blueprint, request, jsonify

user_bp = Blueprint('user', __name__)


@user_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    senha = data.get('senha')

    # Lógica para validar usuário
    # Exemplo fixo (depois vamos consultar o banco)
    if email == 'teste@teste.com' and senha == '123456':
        return jsonify({"mensagem": "Login bem-sucedido!"})
    else:
        return jsonify({"erro": "Usuário ou senha inválidos."}), 401


@user_bp.route('/criar', methods=['POST'])
def criar_usuario():
    data = request.get_json()
    nome = data.get('nome')
    email = data.get('email')
    senha = data.get('senha')

    # Aqui depois a gente conecta no banco e salva
    return jsonify({"mensagem": f"Usuário {nome} criado com sucesso!"})
