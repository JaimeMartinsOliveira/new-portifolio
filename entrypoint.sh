#!/bin/sh

set -e

echo "Ajustando permissões dos diretórios..."
chown -R app:app /app/staticfiles
chown -R app:app /app/media

echo "Aplicando as migrações do banco de dados..."
python manage.py migrate --noinput

echo "Coletando arquivos estáticos..."
python manage.py collectstatic --noinput --clear

# A Mágica Acontece Aqui:
# Executa o comando principal (passado como argumento "$@")
# como o usuário "app"
exec gosu app "$@"