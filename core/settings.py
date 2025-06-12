# core/settings.py (Versão Pronta para Produção)

import os
from pathlib import Path
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(os.path.join(BASE_DIR, '.env'))

# --- Configurações de Segurança ---
# Carrega a SECRET_KEY do ambiente. NUNCA deixe a chave exposta no código.
SECRET_KEY = os.getenv('SECRET_KEY')

# DEBUG deve ser False em produção. Carrega do ambiente.
# A conversão para booleano garante que 'False' ou a ausência da variável resulte em False.
DEBUG = os.getenv('DEBUG', 'False') == 'True'

# Carrega os hosts permitidos do ambiente, separados por vírgula
ALLOWED_HOSTS_str = os.getenv('ALLOWED_HOSTS', '')
ALLOWED_HOSTS = [host.strip() for host in ALLOWED_HOSTS_str.split(',') if host.strip()]


# --- Aplicações e Middlewares ---
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
    'portfolio',
    'captcha',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'captcha.middleware.VisitorNotificationMiddleware',
]

ROOT_URLCONF = 'core.urls'
WSGI_APPLICATION = 'core.wsgi.application'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# --- Templates ---
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# --- Banco de Dados (Configurado para PostgreSQL via Docker) ---
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB'),
        'USER': os.getenv('POSTGRES_USER'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
        'HOST': 'db',  # Nome do serviço do banco de dados no docker-compose.yml
        'PORT': '5432',
    }
}


# --- Arquivos Estáticos e de Mídia ---
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles' # O collectstatic vai juntar os arquivos aqui
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
# Não é mais necessário STATICFILES_DIRS se os arquivos estáticos estiverem dentro das apps


# --- Internacionalização ---
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = True


# --- Validadores de Senha (padrão) ---
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# --- Logging ---
LOGGING = {
    'version': 1, 'disable_existing_loggers': False,
    'formatters': {'verbose': {'format': '{levelname} {asctime} {module} {message}', 'style': '{'}},
    'handlers': {'console': {'class': 'logging.StreamHandler'}, 'file': {'level': 'INFO', 'class': 'logging.FileHandler', 'filename': 'user_access.log', 'formatter': 'verbose'}},
    'loggers': {'user_access': {'handlers': ['file', 'console'], 'level': 'INFO', 'propagate': True}},
}

# --- Segurança Adicional para Produção (quando não estiver em modo DEBUG) ---
if not DEBUG:
    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_SECURE = True
    SECURE_SSL_REDIRECT = True
    SECURE_HSTS_SECONDS = 31536000  # 1 ano
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True