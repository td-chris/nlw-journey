from src.main.server.server import app
# importacao de conexoes
from src.models.settings.db_connection_handler import db_connection_handler

if __name__ == "__main__":
    # Criar conexao com o servidor db antes de subir o server flask
    db_connection_handler.connect()

    app.run(host="0.0.0.0", port=3000, debug=True)

