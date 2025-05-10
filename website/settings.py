import os
import oracledb
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'django-insecure-d7kl((e5wa5e1^%ccvl^a+hvx(==kojegu_^zy!h4@@+em(_2)')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tasks', 
    'website',
    'rest_framework',
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

ROOT_URLCONF = 'website.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'Templates'
        ],
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

WSGI_APPLICATION = 'website.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.oracle',
        'NAME': 'g80ca87422fa593_website_high.adb.oraclecloud.com',
        'USER': 'ADMIN',
        'PASSWORD': 'Sqldeveloper123',
        'HOST': 'adb.sa-santiago-1.oraclecloud.com',
        'PORT': '1522',
        'OPTIONS': {
            'wallet_location': 'C:/Users/vlntn/OneDrive/Escritorio/website-master-main/Wallet_Website'
        }
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
        'OPTIONS': {
            'UserAttributeSimilarityValidator': True,
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 8,  # Mínimo 8 caracteres
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.RegexPasswordValidator',
        'OPTIONS': {
            'regex': r'^(?=.*[!@#$%^&*(),.?":{}|<>])',  # Al menos un carácter especial
            'message': "La contraseña debe contener al menos un carácter especial.",
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.RegexPasswordValidator',
        'OPTIONS': {
            'regex': r'^(?=.*[A-Za-z])(?=.*\d)',  # Al menos una letra y un número
            'message': "La contraseña debe contener al menos una letra y un número.",
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.RegexPasswordValidator',
        'OPTIONS': {
            'regex': r'^.{8,20}$',  # Entre 8 y 20 caracteres
            'message': "La contraseña debe tener entre 8 y 20 caracteres.",
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.RegexPasswordValidator',
        'OPTIONS': {
            'regex': r'^(?=.*[a-z])(?=.*[A-Z])',  # Una letra mayúscula y una minúscula
            'message': "La contraseña debe contener al menos una letra mayúscula y una letra minúscula.",
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.RegexPasswordValidator',
        'OPTIONS': {
            'regex': r'^(?!.*([a-zA-Z0-9])\1{2})',  # Evitar caracteres repetidos
            'message': "La contraseña no debe contener caracteres repetidos tres veces consecutivas.",
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.RegexPasswordValidator',
        'OPTIONS': {
            'regex': r'^(?!.*(?:012|123|234|345|456|567|678|789|abcd|bcde|cdef|defg|efgh|fghi|ghij))',  # Evitar secuencias simples
            'message': "La contraseña no debe contener secuencias numéricas o alfabéticas simples.",
        }
    },
]

# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# Email backend
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'tu_correo@gmail.com'
EMAIL_HOST_PASSWORD = 'tu_contraseña'

