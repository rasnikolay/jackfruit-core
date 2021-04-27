"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 3.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import datetime
import os
from urllib.parse import urlunsplit

from django.utils.timezone import get_current_timezone
from environs import Env
from urllib.parse import urlunsplit
from core.emailer.mailgun_sender import MailGunSender
from core.emailer.stub_sender import StubSender

# Create Env object for getting environment variables
env = Env()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DEBUG', False)

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['localhost', env.str('DOMAIN_NAME', '*')]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'core',
    'bootstrap4',
    'apps.farmer',
    'apps.buyer',
    'apps.store',
    'health_check',
    'health_check.db',
    'django_summernote',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
]

ROOT_URLCONF = 'core.urls'

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

WSGI_APPLICATION = 'core.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': env.dj_db_url('DATABASE_URL')
}

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'ru-RU'
TIME_ZONE = 'Europe/Minsk'

USE_I18N = True
USE_L10N = True
USE_TZ = True

# database ID of the Site object associated with that particular settings file.
# https://docs.djangoproject.com/en/3.0/ref/contrib/sites/#module-django.contrib.sites
SITE_ID = 1

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# STATIC_URL = '/project/apps/core/static'
STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "django.contrib.staticfiles.finders.FileSystemFinder",
)

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
FILE_UPLOAD_PERMISSIONS = 0o644

LOGIN_REDIRECT_URL = 'login'
LOGOUT_REDIRECT_URL = 'login'

AUTH_USER_MODEL = 'core.GreenUser'

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 8,
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Summernote settings
# https://github.com/summernote/django-summernote
X_FRAME_OPTIONS = 'SAMEORIGIN'

# Application settings

VERSION = '1.0.1.10'

STATIC_URL = urlunsplit(("", env.str('STATIC_DOMAIN_NAME'), VERSION + "/", "", ""))

OFFICES_SHORT_NAMES = [
    ('DM3',),
    ('D104',),
    ('D104A',),
    ('F25G',),
    ('KC51A',),
    ('K1/1',),
    ('K1/2',),
    ('K1/5',),
    ('K3',),
    ('K3V',),
    ('N58',),
    ('N177',),
    ('N186',),
    ('P27A',),
    ('R19A',),
    ('S15',),
    ('T150',),
    ('Z29',),
]
OFFICES_SHORT_NAME_CHOICES = tuple(map(lambda x: x * 2, OFFICES_SHORT_NAMES))
DEFAULT_OFFICE = OFFICES_SHORT_NAME_CHOICES[9][0]
OFFICES_SHORT_NAME_LENGTH = 8
DELIVERY_DEADLINE_IN_HOURS = 2
COUNT_ITEMS_ON_DELIVERY_DASHBOARD = 5
IS_REGISTRATION_WITHOUT_ACTIVATING = True
REGISTRATION_WITHOUT_ACTIVATING_DEADLINE = datetime.datetime(2020, 7, 22, 00, 00, tzinfo=get_current_timezone())
SHIPPING_COST = 4
WEIGHT_UNIT_ABBREVIATION = "гр."
CURRENT_CURRENCY = "Br"
CSV_EXPORT_COLUMN_NAMES = {
    "PRODUCTS_IN_DELIVERY": {
        'id': 'id', 'name': 'название', 'price_by_weight': f'цена за вес, {CURRENT_CURRENCY}',
        'total_weight': 'общий вес', 'total_price': 'итого', 'orders_count': 'заказов', 'farmer': 'фермер'
    },
    "ORDERS_IN_DELIVERY": {
        'id': 'id', 'text_delivery': 'Доставка', 'text_user':'Имя', 'total_cost':f'всего, {CURRENT_CURRENCY}',
        'text_total_weight': 'вес', 'home': 'домашний адрес', 'office': 'адрес офиса', 'text_phone': 'Телефон'
    },
    "ORDER_POSITION_IN_DELIVERY": {
        'id': 'id позиции заказа', 'product': 'наименование', 'item_total': f'цена позиции, {CURRENT_CURRENCY}',
        'text_safety_weight': 'вес позиции'
    }
}

if DEBUG:
    mailer = StubSender()
else:
    MAILGUN_API_KEY = env.str('MAILGUN_API_KEY')
    MAILGUN_DOMAIN = env.str('MAILGUN_DOMAIN')
    mailer = MailGunSender(MAILGUN_API_KEY, MAILGUN_DOMAIN)
