from flask import Blueprint, jsonify, request

from models import Usuario

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

@user_bp.route('/listar', methods=['GET'])
def listar_usuario():
    try:
        usuarios = Usuario.query.all()
        resultado = []
        for u in usuarios:
            resultado.append({
                "id": u.id,
                "nome": u.nome,
                "email": u.email,
                "telefone": u.telefone,
                "foto_perfil": u.foto_perfil,
                "tipo_usuario": u.tipo_usuario,
                "ativo": u.ativo,
                "criado_em": u.criado_em.isoformat(),
                "atualizado_em": u.atualizado_em.isoformat()
            })
        return jsonify(resultado)
    except Exception as e:
        return jsonify({"erro": str(e)}), 500