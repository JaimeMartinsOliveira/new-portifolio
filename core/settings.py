from pathlib import Path

# Configuração base do projeto
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-u)t-wixl$5j8j_jqh4@-wp^0^m)emy1@2u-1u4skh%qj3jffr*'
DEBUG = True
ALLOWED_HOSTS = ['15.228.28.91', 'jaimemartins.tech', 'www.jaimemartins.tech', '127.0.0.1']
ROOT_URLCONF = 'core.urls'
WSGI_APPLICATION = 'core.wsgi.application'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Aplicações instaladas
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Suas aplicações
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
]

# Configuração de Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'], # Procure por uma pasta 'templates' na raiz
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

# Base de Dados
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Ficheiros Estáticos e Média
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static', # Procure por uma pasta 'static' na raiz
]
STATIC_ROOT = BASE_DIR / 'staticfiles'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Configuração do Tailwind CSS
TAILWIND_APP_NAME = 'theme'
INTERNAL_IPS = [
    "127.0.0.1",
]

# Internacionalização
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = True

# Validadores de Password
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Logging
LOGGING = {
    'version': 1, 'disable_existing_loggers': False,
    'formatters': {'verbose': {'format': '{levelname} {asctime} {module} {message}', 'style': '{'}},
    'handlers': {'file': {'level': 'INFO', 'class': 'logging.FileHandler', 'filename': 'user_access.log', 'formatter': 'verbose'}},
    'loggers': {'user_access': {'handlers': ['file'], 'level': 'INFO', 'propagate': True}},
}
