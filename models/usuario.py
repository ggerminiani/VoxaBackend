from database.db import db
from sqlalchemy import Enum
from datetime import datetime

class Usuario(db.Model):
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    senha = db.Column(db.String(255), nullable=False)
    telefone = db.Column(db.String(20), nullable=True)
    foto_perfil = db.Column(db.String(255), nullable=True)
    tipo_usuario = db.Column(Enum('admin', 'comum'), nullable=False, default='comum')
    ativo = db.Column(db.Boolean, nullable=False, default=True)

    criado_em = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    atualizado_em = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f"<Usuario {self.nome}>"
