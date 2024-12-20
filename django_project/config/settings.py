"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import os
from pathlib import Path
from datetime import timedelta
from decouple import config
from decouple import Config, RepositoryEnv


# Build paths inside the project like this: BASE_DIR / 'subdir'.
ROOT_DIR = Path(__file__).resolve().parent.parent.parent
BASE_DIR = Path(__file__).resolve().parent.parent

#load .env
config = Config(RepositoryEnv(os.path.join(ROOT_DIR, '.env')))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY', cast=str)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', cast=bool)

if DEBUG:   
    ALLOWED_HOSTS = ['*', 'localhost', '127.0.0.1']
else:
    ALLOWED_HOSTS = [
        config("CORS_ALLOWED_ORIGINS", cast=str),
        config('BACKEND_DOMAIN', cast=str),
        config('CONTAINER_HOSTNAME', cast=str, default=''),
        "localhost",
        "127.0.0.1",
    ]
    
CSRF_TRUSTED_ORIGINS = [
    'http://127.0.0.1', 
    'http://localhost',
    f"https://{config('BACKEND_DOMAIN', cast=str)}", 
    f"http://{config('BACKEND_DOMAIN', cast=str)}",
    f"https://www.{config('BACKEND_DOMAIN', cast=str)}", 
    f"http://www.{config('BACKEND_DOMAIN', cast=str)}",
]

# Application definition
BASE_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

LOCAL_APPS = [
    'utils.apps.UtilsConfig',
    #'core.apps.CoreConfig',
    #'accounts.apps.AccountsConfig',
    'api.apps.ApiConfig',
]
    
PACK_APPS = [
    'rest_framework',
    'rest_framework_simplejwt',
    #'debug_toolbar',
    'drf_spectacular',
    'corsheaders',
    'oauth2_provider',
    'spectacular',
]

INSTALLED_APPS = [*BASE_APPS, *LOCAL_APPS, *PACK_APPS]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'csp.middleware.CSPMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'config.urls'

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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': config('POSTGRES_NAME'),
            'USER': config('POSTGRES_USER'),
            'PASSWORD': config('POSTGRES_PASSWORD'),
            'HOST': config('POSTGRES_HOST'),
            'PORT': config('POSTGRES_PORT'),
        }
    }

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'fa-ir'

TIME_ZONE = 'Asia/Tehran'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'assets'),
]

# Media files
MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media') 

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#this for djdt

INTERNAL_IPS = [
    "127.0.0.1",
]

#RESTFRAMEWORK configure
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}


SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=5),     # Change this to the desired lifetime for the access token
    'REFRESH_TOKEN_LIFETIME': timedelta(days=31),   # Change this to the desired lifetime for the refresh token
    'ROTATE_REFRESH_TOKENS': False,                 # Whether to issue a new refresh token when the refresh token is used
    'BLACKLIST_AFTER_ROTATION': True,               # Whether to blacklist old refresh tokens after rotation
    'UPDATE_LAST_LOGIN': False,                     # Whether to update the last login time when the token is refreshed
}


# your schema drf-spectacular
SPECTACULAR_SETTINGS = {
    'SCHEMA_PATH_PREFIX': r'/api/v1',
    'DEFAULT_GENERATOR_CLASS': 'drf_spectacular.generators.SchemaGenerator',
    'SERVE_PERMISSIONS': ['rest_framework.permissions.AllowAny'],
    'COMPONENT_SPLIT_PATCH': True,
    'COMPONENT_SPLIT_REQUEST': True,
    "SWAGGER_UI_SETTINGS": {
        "deepLinking": True,
        "persistAuthorization": True,
        "displayOperationId": True,
        "displayRequestDuration": True
    },
    'UPLOADED_FILES_USE_URL': True,
    'TITLE': 'BASE DJANGO project Service API',
    'DESCRIPTION': 'Handling user manage endpoint Api',
    'VERSION': '0.2.0',
    'LICENCE': {'name': 'BSD License'},
    'CONTACT': {'name': 'behzad-azadi', 'url': 'https://github.com/behzad-azadi2693'},
    #keycloak SPEC
    'SECURITY': [{
        'name': 'Bearer',
        'scheme': 'bearer',
        'bearerFormat': 'JWT',
    }],
}


#CORS settings
if DEBUG:
    CORS_ORIGIN_ALLOW_ALL = True
else:
    CORS_ALLOWED_ORIGIN_REGEXES = [
         rf"http:\/\/(\w+\.)?{config('CORS_ALLOWED_ORIGINS')}$",
        rf"https:\/\/(\w+\.)?{config('CORS_ALLOWED_ORIGINS')}$",
        rf"^https:\/\/(\w+\.)?{config('BACKEND_DOMAIN')}$",
        rf"^http:\/\/(\w+\.)?{config('BACKEND_DOMAIN')}$"
        ]

CORS_ALLOW_METHODS = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE', 'OPTIONS']
CORS_ALLOW_HEADERS = ['Content-Type', 'Authorization', 'accept', 'user-agent', 'x-csrftoken', 'x-requested-with']
CORS_ALLOW_CREDENTIALS = True



LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'user_manage': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}


#SSL secure for MITM
SECURE_SSL_REDIRECT = not config('DEBUG', cast=bool)
if SECURE_SSL_REDIRECT:
    USE_X_FORWARDED_HOST = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')    
    SECURE_HSTS_SECONDS = 31536000  # 1 year
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True


# Example CSP Directives
CSP_DEFAULT_SRC = ["'self'"]    # Restrict everything to the same origin
CSP_SCRIPT_SRC = ["'self'", "'nonce'"]     # JavaScript sources
CSP_STYLE_SRC = ["'self'", "'nonce'"]      # CSS sources
CSP_IMG_SRC = ["'self'"]        # Image sources
CSP_FONT_SRC = ["'self'"]       # Font sources
CSP_CONNECT_SRC = ["'self'"]    # AJAX, WebSocket
CSP_FRAME_SRC = ["'self'"]      # Frames (e.g., YouTube)
CSP_OBJECT_SRC = ["'none'"]     # Block all plugins
CSP_BASE_URI = ["'self'"]       # Restrict <base> tag
CSP_FORM_ACTION = ["'self'"]  

#add another resource for get data safe
CSP_SCRIPT_SRC += ["'unsafe-inline'", "'unsafe-eval'", "https://cdn.jsdelivr.net", "https://unpkg.com"]
CSP_STYLE_SRC += ["'unsafe-inline'", "https://cdn.jsdelivr.net", "https://unpkg.com"]
CSP_IMG_SRC += ["data:"]
CSP_CONNECT_SRC += [f"https://{config('BACKEND_DOMAIN', cast=str)}", "https://*."]  # Allow Swagger API connections
CSP_CONNECT_SRC += [f"https://{config('CORS_ALLOWED_ORIGINS', cast=str)}"]  # Replace with your actual domain if applicable


CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": f"redis://{config('REDIS_HOST')}:{config('REDIS_PORT', cast=int)}/1",
        'OPTIONS': {
            'PASSWORD': config('REDIS_PASSWORD'),
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}
