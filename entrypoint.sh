#!/bin/sh

set -e

# Cria as pastas necessárias, se não existirem
mkdir -p /app/logs
mkdir -p /app/staticfiles
mkdir -p /app/media

# Ajusta as permissões para o usuário 'app'
echo "Ajustando permissões dos diretórios..."
chown -R app:app /app/staticfiles
chown -R app:app /app/media
chown -R app:app /app/logs # <-- ESTA LINHA É FUNDAMENTAL

# Aplica as migrações do banco de dados
echo "Aplicando as migrações do banco de dados..."
python manage.py migrate --noinput

# Coleta os arquivos estáticos
echo "Coletando arquivos estáticos..."
python manage.py collectstatic --noinput --clear

# Inicia o servidor Gunicorn
echo "Iniciando o servidor Gunicorn como usuário 'app'..."
exec gosu app "$@"