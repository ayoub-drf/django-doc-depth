"""
Django settings for dj project.

Generated by 'django-admin startproject' using Django 5.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-l*323nfa=h7yd^n1#=zpkjxbr3&4mpc$qe1hn65^&#z8rjdyh!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG =True

ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'debug_toolbar',

    'new_models',
    'new_querysets',
    'new_migrations',
    'new_managers',
    'new_transactions',
    'new_aggregation',
    'new_mult_databases',
    'new_custom_lookups',
    'new_query_expressions',
    'new_database_functions',
    'new_fixtures',
    'new_URLconfs',
    'new_shortcut_functions',
    'new_view_decorators',
    'Asynchronous_support',
    'req_res_obj',
    'file_uploads',
    'class_based_views',
    'csv_output',
    'pdf_output',
    'middleware_1',
    'template_filters',
    'django.contrib.humanize',w
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware', # done
    'django.contrib.sessions.middleware.SessionMiddleware', # done
    'django.middleware.common.CommonMiddleware', # done
    'django.middleware.csrf.CsrfViewMiddleware', # done
    'django.contrib.auth.middleware.AuthenticationMiddleware', # Done
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "debug_toolbar.middleware.DebugToolbarMiddleware",

    # 'middleware_1.middlewares.LoggerViewMiddleWare',
    # 'middleware_1.middlewares.SimpeMiddleWare',
    'middleware_1.middlewares.simple_middleware_two',

    # 'django.middleware.locale.LocaleMiddleware', # done
    # 'django.middleware.gzip.GZipMiddleware' # done
    # 'django.middleware.cache.CacheMiddleware' # done
    # 'django.middleware.transaction.TransactionMiddleware' # done
]

INTERNAL_IPS = [
    "127.0.0.1",
]

ROOT_URLCONF = 'dj.urls'

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

WSGI_APPLICATION = 'dj.wsgi.application'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        },
        'class_based_views': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        },
        'middleware_1': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}



# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
    'secondary': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'second.sqlite3',
    },
}

DATABASE_ROUTERS = ['new_mult_databases.routers.MyRouter']

# DATABASES =  {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'mydb',
#         'USER': 'root',
#         'PASSWORD': 'admin',
#         'HOST': 'localhost',
#         'PORT': 3306,
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]


MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

MAX_UPLOAD_SIZE = 10485760

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
