"""
Django settings for CypherDesk project.

Generated by 'django-admin startproject' using Django 2.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
HOSTNAME = 'http://cypherdesk.tk:8000/'
SERVER_IP = '195.123.213.226' 

#isyn.tk ip -> 195.123.225.209
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#r394am$y(&xrwvxye27ny%d45_f-*g3sc7t7203nwp71%$7n%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'cypherdesk.ru', '37.230.112.63']

# EMAIL settings
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'cypherdesk.isyn@gmail.com'
EMAIL_HOST_PASSWORD = 'HackersChoose1syn'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# GOOGLE RECAPTCHA
GOOGLE_RECAPTCHA_SITE_KEY = '6LdFjF8UAAAAAF7w-ZN0QNLIgMyCLjBvZE4_FLlO'
GOOGLE_RECAPTCHA_SECRET_KEY = '6LdFjF8UAAAAAHVxsXjpm7ZHKjMrxc5pUM9bc2v3'

# Telegram Bot
FEEDBACK_TELEGRAM_BOT_KEY = {'feedback': '502481144:AAF0Nww9QBmwCJMKAtmuCwR_RZ7NpGqPBsQ', }
FEEDBACK_TELEGRAM_CHAT_ID = {'feedback': -1001173635794, }

# Application definition

INSTALLED_APPS = [
    'AdminPanel',
    'News',
    'g_recaptcha',
    'LandPage',
    'Feedback',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'CypherDesk.urls'

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

WSGI_APPLICATION = 'CypherDesk.wsgi.application'
DEFAULT_CHARSET = 'utf-8'

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# мы ПОКА не гарантируем, что cookies передаются по https, поэтому, чтобы не вылетала ошибка 403 или csrf-exception, оставляем значение False
CSRF_COOKIE_SECURE = False
# SESSION_SAVE_EVERY_REQUEST = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(BASE_DIR, "static")
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
