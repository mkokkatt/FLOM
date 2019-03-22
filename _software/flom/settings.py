"""
Django settings for flom project.

Generated by 'django-admin startproject' using Django 2.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import json
from django.core.cache import cache

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CONFIG_FILE = 'config.ini'
config = {}
with open(CONFIG_FILE) as f:
    config = json.load(f)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# if config['DEVELOPMENT'] == "True":
#     print("IN DEV MODE")
#     from . import sample_data_loader as sdl
#     sdl.create_tables(config['DATABASES']['default'])
#     sdl.insert_occupancy(config['DATABASES']['default'])
#     print('finished sdl')

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'library_monitor.apps.LibraryMonitorConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'database'
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

ROOT_URLCONF = 'flom.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'flom.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE' : 'django.db.backends.postgresql',
        'NAME' : 'FLOM',
        'USER' : 'FLOM',
        'PASSWORD' : 't7ZsHPj7W4gC5Fy',
        'HOST' : 'flom.chko6eajdpxb.us-east-1.rds.amazonaws.com',
        'PORT' : '5432'
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'EST'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# SESSION_COOKIE_SECURE = True
# SECURE_SSL_REDIRECT = True
# CSRF_COOKIE_SECURE = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

cache.set('SECRET_KEYs', set(config['SECRET_KEYs'].keys()), None)

for floor in config['FLOOR']:
    rooms = config['FLOOR'][floor]
    cache.set('floor_' + floor, rooms, None)
    for room_id in rooms:
        cache.set(room_id, False, None)

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# collectstatic directory
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
