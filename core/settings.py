import os
from pathlib import Path

# Caminho base do projeto
BASE_DIR = Path(__file__).resolve().parent.parent

# --- CONFIGURAÇÕES DE SEGURANÇA ---

# Se houver variável de ambiente, usa. Caso contrário, gera um warning
SECRET_KEY = os.getenv(
    'DJANGO_SECRET_KEY',
    'django-insecure-change-this-in-production-never-use-in-live'
)

# DEBUG é True no seu PC, mas será False quando configurarmos o Railway
DEBUG = os.getenv('DJANGO_DEBUG', 'True').lower() == 'true'

# Configurar hosts permitidos
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '*').split(',')

# Configurar CSRF trusted origins para segurança
CSRF_TRUSTED_ORIGINS = os.getenv('CSRF_TRUSTED_ORIGINS', 'http://localhost:8000').split(',')


# --- DEFINIÇÃO DO APLICATIVO ---

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'catalogo.apps.CatalogoConfig',
    'usuarios.apps.UsuariosConfig',
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

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


# --- BANCO DE DADOS ---

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# --- VALIDAÇÃO DE SENHA ---

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# --- INTERNACIONALIZAÇÃO ---

LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = True


# --- ARQUIVOS ESTÁTICOS E MÍDIA ---

STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
# Pasta onde o servidor vai reunir todos os arquivos estáticos no deploy
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# --- REDIRECIONAMENTOS ---

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

# --- SEGURANÇA EXTRA PARA PRODUÇÃO ---
if not DEBUG:
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    X_FRAME_OPTIONS = 'DENY'
    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_SECURE = True
    SECURE_SSL_REDIRECT = True
    
    # Adiciona HTTPS se não estiver em modo debug
    if not os.getenv('ALLOW_HTTP'):
        SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')