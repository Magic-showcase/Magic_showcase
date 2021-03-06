"""
Django settings for Integradora project.

Generated by 'django-admin startproject' using Django 3.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import cloudinary
import cloudinary.uploader
import cloudinary.api

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'admin132'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
    
ALLOWED_HOSTS = ['*']

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Nucleo',
    'Control_Vi',
    'Tienda',
    'Blog',
    'Usuario',
    'Preguntas',
    'cloudinary',
    'paypalcheckoutsdk',
    'Tutorial',
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
    'Integradora.middleware.veriperfil',
]

ROOT_URLCONF = 'Integradora.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
             #directorio de mis plantillas
            BASE_DIR / 'Templates',
            BASE_DIR / 'Tienda/Templates',
            BASE_DIR / 'Blog/Templates',
            BASE_DIR / 'Usuario/Templates',
            BASE_DIR / 'Control_Vi/Templates',
            BASE_DIR / 'Preguntas/Templates',
            BASE_DIR / 'Tutorial/Templates',
        ],
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

WSGI_APPLICATION = 'Integradora.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

else:
    import dj_database_url
    from decouple import config

    DATABASES = {
        'default':
            dj_database_url.config(
                default=config('DATABASE_URL')
            )
    }


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'


TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'







#carpeta para media 
MEDIA_URL = '/media/'
#Donde buscar los archivos multimedia
MEDIA_ROOT=BASE_DIR / 'media'
#Constante
#STATICFILES_STORAGE='whitenoise.storage.CompressedManifestStaticFilesStorage'
#SERVIDOR EMAIL
EMAIL_BACKEND="django.core.mail.backends.smtp.EmailBackend"
#Espesificar el host
EMAIL_HOST="smtp.gmail.com"
#Protocolo de seguridad

EMAIL_USE_TLS=True

#Puerto

EMAIL_PORT=587

#Cuenta 

EMAIL_HOST_USER="Magic.showcase.questions@gmail.com"

EMAIL_HOST_PASSWORD="bajfgpcgwwzeqend"

DEFAUL_FROM_EMAIL = 'Magic Showcase password'


#configuracion cloudinary

cloudinary.config( 
  cloud_name = "dlwkmbywp", 
  api_key = "633139964856883", 
  api_secret = "VENOMPMHeETWXUVhYQe9MB2ap94" 
)

