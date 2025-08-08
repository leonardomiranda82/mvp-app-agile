import os
from flask import Flask, jsonify
from flask_cors import CORS
import psycopg2
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env
load_dotenv()

# Cria a aplicação Flask
app = Flask(__name__)
# Habilita o CORS, permitindo que nosso frontend (em outra porta) faça requisições
CORS(app) 

# Função auxiliar para criar uma conexão com o banco
def get_db_connection():
    conn = psycopg2.connect(os.getenv('DATABASE_URL'))
    return conn

# Define a nossa rota de API: http://localhost:5000/api/message
@app.route('/api/message')
def get_hello_message():
    try:
        # Tenta se conectar e buscar a mensagem
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT message_text FROM messages WHERE id = 1;')
        # Pega o primeiro resultado da busca
        message = cur.fetchone()[0]
        cur.close()
        conn.close()
        # Retorna a mensagem em formato JSON
        return jsonify({'message': message})
    except Exception as e:
        # Em caso de erro, retorna uma mensagem de erro
        print(f"Erro na API: {e}")
        return jsonify({'error': str(e)}), 500

# Esta parte só executa quando rodamos o script diretamente
if __name__ == '__main__':
    # Inicia o servidor na porta 5000, acessível por qualquer IP na rede
    app.run(host='0.0.0.0', port=5000)