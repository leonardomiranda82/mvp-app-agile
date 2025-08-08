# 1. Comece com uma imagem base leve do Python 3.9
FROM python:3.9-slim

# 2. Defina o diretório de trabalho dentro do container
WORKDIR /app

# 3. Copie o arquivo de dependências para o container
COPY requirements.txt .

# 4. Instale as dependências
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copie todo o resto do código do backend para o container
COPY . .

# 6. Defina o comando que será executado quando o container iniciar
CMD ["python", "app.py"]