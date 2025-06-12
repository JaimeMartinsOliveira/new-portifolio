# Dockerfile

# 1. Use uma imagem base oficial do Python
FROM python:3.11-slim

# 2. Defina variáveis de ambiente para o Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 3. Crie e defina o diretório de trabalho dentro do contêiner
WORKDIR /app

# 4. Instale as dependências
# Copia primeiro o requirements.txt para aproveitar o cache do Docker
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copie o resto do código do seu projeto para o diretório de trabalho
COPY . /app/

# 6. Exponha a porta que a aplicação irá rodar (usada pelo Gunicorn)
EXPOSE 8000