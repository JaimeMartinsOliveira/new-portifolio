#!/bin/sh

set -e

mkdir -p /app/logs
mkdir -p /app/staticfiles
mkdir -p /app/media

echo "Ajustando permissões dos diretórios..."
chown -R app:app /app/staticfiles
chown -R app:app /app/media
chown -R app:app /app/logs

echo "Aplicando as migrações do banco de dados..."
python manage.py migrate --noinput

echo "Coletando arquivos estáticos..."
python manage.py collectstatic --noinput --clear

echo "Iniciando o servidor Gunicorn como usuário 'app'..."
exec gosu app "$@"