import os
from pathlib import Path
from dotenv import load_dotenv
import dj_database_url

load_dotenv()  # Carrega as variáveis do arquivo .env

BASE_DIR = Path(__file__).resolve().parent.parent


# Segurança
SECRET_KEY = os.getenv('SECRET_KEY', 'fallback-secret-key-para-dev')

DEBUG = os.getenv('DEBUG', 'False').lower() in ['true', '1', 'yes']

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '').split(',')





# Aplicações instaladas
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tasks',
    'users',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR],  # mantendo templates na raiz do projeto
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

WSGI_APPLICATION = 'backend.wsgi.application'


# Banco de dados
DATABASES = {
    'default': dj_database_url.config(conn_max_age=600)
}



# Validação de senha
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


AUTH_USER_MODEL = 'users.User'


# Internacionalização
LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

CSRF_TRUSTED_ORIGINS = ['https://doitnow.up.railway.app']

# Arquivos estáticos
STATIC_URL = 'static/'

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'),]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# Tipo padrão de chave primária
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
