import os

from flask_sqlalchemy import SQLAlchemy
import urllib.parse

db = SQLAlchemy()

HOST = os.getenv('DB_HOST')
PORT = os.getenv('DB_PORT')
PASS = os.getenv('DB_PASS')
USER = os.getenv('DB_USER')
NAME = os.getenv('DB_NAME')
URI = f"mysql+pymysql://{USER}:{urllib.parse.quote(PASS)}@{HOST}:{PORT}/{NAME}"

def init_db(app):
    print("URI", URI)

    if not URI:
        raise ValueError("DB_URL não encontrado no arquivo .env")

    app.config['SQLALCHEMY_DATABASE_URI'] = URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    print("✅ Banco de dados conectado com sucesso!")

