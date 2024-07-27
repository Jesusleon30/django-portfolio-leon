
from datetime import timedelta
from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-vyi50rltr=hdf2^naqy4ux&j-*3%*nuu+o*eqr443gj2h=2@h4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#ALLOWED_HOSTS = []    #default

ALLOWED_HOSTS = ['*']
# ojo en esta parte es solo de prueva 
# aca tendriamos que poner el localstore solo del puerto de nuestro servidor 
# poniendo el * estamos diciendo que qualquiera puede manrdarnos datos desde qualquier servidor web y eso no esta bien
# una vez terminado la prueva elimniar el '*' y poner el puerto de nuestro servidor oficial 


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'cloudinary_storage',
    'cloudinary',
    'rest_framework',
    'tasks',
    'users',
    'storeapp',
    'immagini',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

#comentario
# CORS_ORIGIN_WHITELIST = (
#     'http://localhost',
# )



ROOT_URLCONF = 'portfolio_todo_list_api.urls'

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

WSGI_APPLICATION = 'portfolio_todo_list_api.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        "ENGINE": os.environ["ENGINE"],
        "NAME": os.environ["NAME"],
        "USER": os.environ["USER"],
        "PASSWORD": os.environ["PASSWORD"],
        "HOST": os.environ["HOST"]
    }
}




# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = "Europe/Rome"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# DEFAULT_AUTO_FIELD = True;

# REST_FRAMEWORK = {
#     'DEFAULT_AUTHENTICATION_CLASSES': (
#         'rest_framework_simplejwt.authentication.JWTAuthentication',
#     )
# }

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(weeks=4)  # days=365*100 => 100 años
}


CORS_ALLOW_ALL_ORIGINS = True

import os
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media') 





# mis credenciales de cloudinary
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage' 
# este es la ruta en la nube www.cloudinary.....

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'df43ck7uo',
    'API_KEY': '598568871622394',
    'API_SECRET': 'Jog2-LGioYzTYjJsZ1H6ors7rDA',
}

STATIC_ROOT = BASE_DIR/'static'
