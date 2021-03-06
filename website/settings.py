"""
Django settings for china project.
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'cao6_8kd&1+_k42gm0gvhx36!idz1-jexggr3^d=b=@wmxy@od'

WHITENOISE_MAX_AGE = 31557600
WHITENOISE_ALLOW_ALL_ORIGINS = False

DEBUG = False
ALLOWED_HOSTS = ["*"]
APPEND_SLASH = True

# Application definition
INSTALLED_APPS = [
    'django.contrib.auth',
    'django_openid_auth',
    'bootstrap_admin',  # always before django.contrib.admin
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_markdown',
    'markdown_deux',
    'website',
    'reversion',
    'reversion_compare',
    'django_versioned_static_url',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
]

ROOT_URLCONF = 'website.urls'

STATICFILES_FINDERS = [
    'django_static_root_finder.finders.StaticRootFinder',
    "django.contrib.staticfiles.finders.AppDirectoriesFinder"
]
STATIC_ROOT = 'static'
STATIC_URL = '/static/'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request'
            ],
        },
    },
]
MARKDOWN_DEUX_STYLES = {
    "default": {
        "extras": {
            "code-friendly": None,
        },
        "safe_mode": False,
    },
}
WSGI_APPLICATION = 'website.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'dev',
        'HOST': 'db',
        'PORT': '5432',
    }
}

# Update database settings from DATABASE_URL environment variable
import dj_database_url
DATABASES['default'].update(dj_database_url.config())

# Django openID auth
# ===

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'

AUTHENTICATION_BACKENDS = (
    'django_openid_auth.auth.OpenIDBackend',
    'django.contrib.auth.backends.ModelBackend',
)

LOGIN_URL = '/openid/login/'
LOGIN_REDIRECT_URL = '/'

SUPERUSER_GROUP = 'canonical-webmonkeys'
GROUP_PERMISSIONS = [
    'change_element',
    'change_page',
    'add_revision',
    'change_revision',
    'delete_revision',
    'add_version',
    'change_version',
    'delete_version'
]

OPENID_CREATE_USERS = True
OPENID_SSO_SERVER_URL = 'https://login.launchpad.net/'
OPENID_LAUNCHPAD_TEAMS_REQUIRED = [
    'canonical-content-people',
    'canonical-webmonkeys'
]
OPENID_USE_AS_ADMIN_LOGIN = True
OPENID_LAUNCHPAD_TEAMS_MAPPING_AUTO = True

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

from django.utils.translation import ugettext_lazy
LANGUAGES = (('zh-hans', ugettext_lazy('Chinese')),)
LANGUAGE_CODE = 'zh-hans'
LOCALE_PATHS = [os.path.join(BASE_DIR, 'locale/')]

TIME_ZONE = 'Asia/Shanghai'
USE_I18N = True
USE_L10N = True
USE_TZ = True
