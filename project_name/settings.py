import os
import dj_database_url

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = "n$i_!u=@bf00m-v8d*#erjsxqxwkgiiz(wdzquzg6!bld9h+wk"
DEBUG = True
SITE_ID = 1

ROOT_URLCONF = '{{ project_name }}.urls'

DATABASES = {'default': dj_database_url.config(default='postgres://@localhost/{{ project_name }}')}

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages'
]

MIDDLEWARE_CLASSES = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    "django.contrib.flatpages.middleware.FlatpageFallbackMiddleware",
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
]

MEDIA_ROOT = '/tmp/media/'
MEDIA_URL = '/media/'

STATIC_ROOT = '/tmp/static/'
STATIC_URL = '/static/'