# Use a imagem oficial do Python
FROM python:3.10-slim

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos do projeto para dentro do container
COPY . /app

# Instala as dependências
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Expõe a porta que o Django vai rodar
EXPOSE 8000

# Comando para rodar o servidor Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
