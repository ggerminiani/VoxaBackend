import os

from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

load_dotenv()
HOST = os.getenv('DB_HOST')
PORT = os.getenv('DB_PORT')
PASS = os.getenv('DB_PASS')
USER = os.getenv('DB_USER')
NAME = os.getenv('DB_NAME')
URI = f"mysql+pymysql://{USER}:{PASS}@{HOST}:{PORT}/{NAME}"


def init_db(app):
    print("URI", URI)

    if not URI:
        raise ValueError("DB_URL não encontrado no arquivo .env")

    app.config['SQLALCHEMY_DATABASE_URI'] = URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    print("✅ Banco de dados conectado com sucesso!")


def test_db_connection():
    try:
        print("URI", URI)
        with db.engine.connect() as connection:
            result = connection.execute("SELECT 1")
            print("✅ Teste de conexão com o banco bem-sucedido!")
            return True
    except Exception as e:
        print(f"❌ Erro ao conectar no banco: {str(e)}")
        return False
