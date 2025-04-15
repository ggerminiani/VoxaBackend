import os

from flask import Blueprint, request, jsonify

from transcricao.transcrever import transcrever_audio

transcript_bp = Blueprint('transcript', __name__)


@transcript_bp.route('/transcrever', methods=['POST'])
def transcrever():
    if 'audio' not in request.files:
        return jsonify({"erro": "Arquivo de áudio não enviado"}), 400

    arquivo = request.files['audio']

    caminho_uploads = "uploads"
    if not os.path.exists(caminho_uploads):
        os.makedirs(caminho_uploads)

    caminho_arquivo = os.path.join(caminho_uploads, arquivo.filename)
    arquivo.save(caminho_arquivo)

    try:
        texto_transcrito = transcrever_audio(caminho_arquivo)
        return jsonify({"transcricao": texto_transcrito})
    except Exception as e:
        return jsonify({"erro": str(e)}), 500
