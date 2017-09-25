#coding: utf-8

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$@-)zwh*^e3#z-r@8q414uy1p(6&4q-2129e4kpvw##_4=)foe'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'gestaoapp',
    'gestaoapp.templatetags',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'gestao.urls'

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

WSGI_APPLICATION = 'gestao.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',  # Add 'post$
        'NAME': 'sgp',  # Or $
        'USER': 'sgp',  # Not$
        'PASSWORD': 'sgp.7@ifc',  # Not$
        'HOST': 'banco.fabricadesoftware.ifc.edu.br',
        'PORT': '5432',  # Set to empt$
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }
#

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

LOGIN_REDIRECT_URL = '/home/'
# MEDIA_ROOT = '/var/www/gestao/static'
STATIC_URL = '/static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # Absolute path to the media directory

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s' #You may need to specify the timezone here. For example: %(asctime)s CST [%(levelname)s] %(name)s: %(message)s
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'null': {
            'level':'DEBUG',
            'class':'django.utils.log.NullHandler',
        },
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler'
        },
        'default': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            #'filename': 'app.log',  Make sure that this path exists, change as necessary
            'filename': 'gestao.log',
            'maxBytes': 1024*1024*5, # 5 MB
            'backupCount': 5,
            'formatter':'standard',
        }
    },
    'loggers': {
        'django.db': {
            'handlers': ['default'],
            'level': 'DEBUG', # Set this to ERROR on production hosts since the database logs are very verbose
            'propagate': False, 
        },
        '': {
            'handlers': ['default'],
            'level': 'DEBUG',
            'propagate': True,
        },

        'django.request': {
            'handlers': ['default'],
            'level': 'DEBUG', # Set this to ERROR on production hosts if you want to avoid lots of warnings for 404 file-not-found notices
            'propagate': False,
        },
    }
}
