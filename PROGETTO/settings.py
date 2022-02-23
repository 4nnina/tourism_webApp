"""
Django settings for PROGETTO project.

Generated by 'django-admin startproject' using Django 3.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
from pathlib import Path
from django.contrib.gis.gdal import OGRGeometry
import os

import platform
import environ

WINDOWS = platform.system() == "Windows"

if WINDOWS:
    # the below needs to change for linux
    GDAL_LIBRARY_PATH = r'C:\OSGeo4W\bin\gdal303.dll'
    GEOS_LIBRARY_PATH = r'C:\OSGeo4W\bin\geos_c.dll'
    OSGEO4W = r"C:\OSGeo4W"
    os.environ['OSGEO4W_ROOT'] = OSGEO4W
    os.environ['GDAL_DATA'] = "C:\Program Files\GDAL\gdal-data"  # OSGEO4W + r"\share\gdal"
    os.environ['PROJ_LIB'] = OSGEO4W + r"\share\proj"
    os.environ['PATH'] = OSGEO4W + r"\bin;" + os.environ['PATH']

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

#  use this if setting up on Windows 10 with GDAL installed from OSGeo4W using defaults
#if os.name == 'nt':
 #   VIRTUAL_ENV_BASE = os.environ['VIRTUAL_ENV']
 #   os.environ['PATH'] = os.path.join(VIRTUAL_ENV_BASE, r'.\Lib\site-packages\osgeo') + ';' + os.environ['PATH']
 #   os.environ['PROJ_LIB'] = os.path.join(VIRTUAL_ENV_BASE, r'.\Lib\site-packages\osgeo\data\proj') + ';' + os.environ['PATH']
#See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-i7v8wo3l4n@a&332a95qf$9$t$5wutt*ovoj!hqd%x$nm=)65n'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#ALLOWED_HOSTS = ['localhost']
ALLOWED_HOSTS=['127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'tourismApp.apps.TourismappConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'ckeditor',
    'django.contrib.sites',
    #'leaflet',
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

ROOT_URLCONF = 'PROGETTO.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.jinja2.Jinja2',
        #'DIRS': [os.path.join(BASE_DIR, 'templates/jinja2')],
        'APP_DIRS': True,
        #'OPTIONS': {'environment': 'myproject.jinja2.Environment',},
    },
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'PROGETTO.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME':'tourismdb',
        'USER':'postgres',
        'PASSWORD':'pa55w0rd',
        'HOST':'localhost',
        'PORT':'5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Rome'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
#STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'), )

#MEDIA_URL = '/media/'
#MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar':  [
            ['Styles', 'Format', 'Bold', 'Italic', 'Underline', 'Strike', 'SpellChecker', 'Undo', 'Redo'],
            ['TextColor', 'BGColor'],
            ['NumberedList','BulletedList'],
            ['JustifyLeft','JustifyCenter','JustifyRight','JustifyBlock'],
            ['Indent','Outdent'],
            [ 'SpecialChar'],
            #['Source'],
        ],
        #'height': 300,
        'width': 750,
    },
}

LEAFLET_CONFIG = {
    # conf here
    #'SPATIAL_EXTENT': (10.0, 44.0, 10.5, 46),
    #'DEFAULT_CENTER': (45.44, 10.999),
    #'DEFAULT_ZOOM': 14,
    #'MIN_ZOOM': 3,
    #'MAX_ZOOM': 18,
    #'DEFAULT_PRECISION': 6,
}

#GDAL_LIBRARY_PATH = r'C:\OSGeo4W64\bin\gdalplugins'
#os.environ['GDAL_DATA'] = "C:\\OSGeo4W64\\share\\epsg_csv" <- (path to gcs.csv file)