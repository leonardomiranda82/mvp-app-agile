# backend/app.py
import os
from flask import Flask, jsonify, request
from flask_cors import CORS
import psycopg2
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
CORS(app)

def get_db_connection():
    conn = psycopg2.connect(os.getenv('DATABASE_URL'))
    return conn

# Rota para GET (todos) e POST (criar)
@app.route('/api/messages', methods=['GET', 'POST'])
def handle_messages():
    if request.method == 'POST':
        # ... (código para criar mensagem, sem alterações)
        data = request.get_json()
        new_message = data['message']
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO messages (message_text) VALUES (%s)', (new_message,))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'status': 'success', 'message': 'Message created'}), 201
    else: # GET
        # ... (código para buscar todas as mensagens, sem alterações)
        try:
            conn = get_db_connection()
            cur = conn.cursor()
            cur.execute('SELECT id, message_text FROM messages ORDER BY id ASC;')
            messages_raw = cur.fetchall()
            cur.close()
            conn.close()
            messages_list = [{'id': row[0], 'text': row[1]} for row in messages_raw]
            return jsonify(messages_list)
        except Exception as e:
            print(f"Erro na API: {e}")
            return jsonify({'error': str(e)}), 500

# NOVA ROTA: Rota para DELETE de uma mensagem específica
@app.route('/api/messages/<int:message_id>', methods=['DELETE'])
def delete_message(message_id):
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        # Executa o comando SQL para deletar a linha com o ID correspondente
        cur.execute('DELETE FROM messages WHERE id = %s;', (message_id,))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'status': 'success', 'message': f'Message {message_id} deleted'}), 200
    except Exception as e:
        print(f"Erro ao deletar: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)