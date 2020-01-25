import os
from decouple import (
    config,
    Csv
)
import dj_database_url

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = config(
    'DUAL_ROCKS_SECRET_KEY',
    default='@gp6r9ma%dun36-z26@m*e+1hqvzykv34=_)bx7^i9#!z@x3kf'
)

DEBUG = config(
    'DUAL_ROCKS_DEBUG',
    cast=bool,
    default=True
)

ALLOWED_HOSTS = config(
    'DUAL_ROCKS_ALLOWED_HOSTS',
    default='',
    cast=Csv()
)


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'dual_rocks.authentication',
    'dual_rocks.web',
    'bulma',
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

ROOT_URLCONF = 'dual_rocks.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'dual_rocks.wsgi.application'


# Database

DATABASES = {
    'default': dj_database_url.config(
        default=config(
            'DUAL_ROCKS_DEFAULT_DATABASE',
            default='sqlite:///db.sqlite3'
        )
    )
}


# Auth

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.'
        'UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
        'MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
        'CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
        'NumericPasswordValidator',
    },
]

AUTH_USER_MODEL = 'authentication.User'

LOGIN_URL = 'web:login'

LOGIN_REDIRECT_URL = 'web:home'

LOGOUT_REDIRECT_URL = 'web:home'


# Internationalization

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "assets")
]

STATIC_URL = '/static/'
