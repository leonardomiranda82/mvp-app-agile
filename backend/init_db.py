import os
import psycopg2
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env para a memória
load_dotenv()

print("Conectando ao banco de dados PostgreSQL...")
# Usa a DATABASE_URL do nosso .env para conectar
conn = psycopg2.connect(os.getenv('DATABASE_URL'))
cur = conn.cursor()
print("Conexão bem-sucedida.")

# Apaga a tabela 'messages' se ela já existir, para começar do zero
cur.execute('DROP TABLE IF EXISTS messages;')

# Cria a tabela 'messages' com uma coluna para id e uma para o texto
print("Criando a tabela 'messages'...")
cur.execute('CREATE TABLE messages (id serial PRIMARY KEY,'
                                 'message_text varchar (150) NOT NULL);')

# Insere nossa mensagem de teste na tabela
print("Inserindo a mensagem inicial...")
cur.execute('INSERT INTO messages (message_text)'
            'VALUES (%s)',
            ('Helo World escrito no PostgreSQL!',))

# Salva as alterações no banco de dados
conn.commit()

# Fecha a comunicação
cur.close()
conn.close()

print("Banco de dados 'mvp_db' inicializado com sucesso!")