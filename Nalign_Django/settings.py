"""
Django settings for Nalign_Django project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from django.core.urlresolvers import reverse_lazy
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=+)n-b_j4u23%#7qkhmmcc%$eg!9jh=50j8-&0tk2l6d73!522'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

LOGIN_URL = reverse_lazy('login')
LOGIN_REDIRECT_URL = reverse_lazy('home')

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'gunicorn',
    'nalign_app_recorder',
    'south',
    'rest_framework',
    'provider', 
    'provider.oauth2',
    'webservice',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

STATICFILES_DIRS = (
#Static files in different directories
	os.path.join(BASE_DIR, "static"),
	"/opt/myenv/Nalign_Django/Nalign_Django/static/", 
	"/opt/myenv/Nalign_Django/nalign_app_recorder/static/",
)

STATICFILES_FINDERS = ( 
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': 
        ('rest_framework.authentication.OAuth2Authentication',
         'rest_framework.authentication.SessionAuthentication'),
    'DEFAULT_MODEL_SERIALIZER_CLASS':
        'rest_framework.serializers.ModelSerializer',
    'DEFAULT_PERMISSION_CLASSES': 
        ('rest_framework.permissions.IsAdminUser' ,
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',),

    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.YAMLParser',
    )
}


ROOT_URLCONF = 'Nalign_Django.urls'

WSGI_APPLICATION = 'Nalign_Django.wsgi.application'

PROJECT_DIR = os.path.dirname(__file__)

TEMPLATE_DIRS = (
	
	os.path.join(PROJECT_DIR, '../templates/Nalign_Django'),
	os.path.join(PROJECT_DIR, '../templates/nalign_app_recorder'),
)


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': 'mydb',                      # Or path to database file if using sqlite3.
            # The following settings are not used with sqlite3:
            'USER': 'kthuser',
            'PASSWORD': 'kthuser',
            'HOST': 'localhost',                      # Empty for localhost through domain sockets or           '127.0.0.1' for localhost thrgh TCP.
            'PORT': '',                      # Set to empty string for default.
        }
    }


SESSION_ENGINE= (
	"django.contrib.sessions.backends.file"
	)
# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT =''
#"/opt/myenv/static/admin"

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
