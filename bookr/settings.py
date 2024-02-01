"""
Django settings for bookr project.

Generated by 'django-admin startproject' using Django 3.0a1.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

import os
import django_heroku
import dj_database_url
from decouple import config

from configurations import Configuration, values


class Dev(Configuration):
    # Build paths inside the project like this: os.path.join(BASE_DIR, ...)
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Quick-start development settings - unsuitable for production
    # See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = 'y%ux@_^+#eahu3!^i2w71qtgidwpvs^o=w2*$=xy+2-y4r_!fw'

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = values.BooleanValue(True)

    ALLOWED_HOSTS = values.ListValue([])

    # Application definition

    INSTALLED_APPS = [
        'bookr_admin.apps.BookrAdminConfig',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'rest_framework',
        'rest_framework.authtoken',
        'reviews',
        'book_management',
        'bookr_admin',
        'debug_toolbar',
        'crispy_forms'
    ]
    SITE_ID = 1

    MIDDLEWARE = [
        'debug_toolbar.middleware.DebugToolbarMiddleware',
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        'whitenoise.middleware.WhiteNoiseMiddleware',
    ]

    ROOT_URLCONF = 'bookr.urls'

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
                    'django.template.context_processors.media'
                ],
            },
        },
    ]

    WSGI_APPLICATION = 'bookr.wsgi.application'

    # Database
    # https://docs.djangoproject.com/en/dev/ref/settings/#databases

    DATABASES = values.DatabaseURLValue(
        'sqlite:///{}/db.sqlite3'.format(BASE_DIR),
        environ_prefix='DJANGO'
    )

    # Password validation
    # https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators

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
    # https://docs.djangoproject.com/en/dev/topics/i18n/

    LANGUAGE_CODE = 'en-us'

    TIME_ZONE = 'UTC'

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/dev/howto/static-files/

    STATIC_URL = '/static/'

    STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
    
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    MEDIA_URL = '/media/'
    INTERNAL_IPS = ['127.0.0.1']
    CRISPY_TEMPLATE_PACK = 'bootstrap4'
    


class Prod(Dev):
    DEBUG = False
    SECRET_KEY = values.SecretValue()
    
django_heroku.settings(locals())
