from os.path            import join, dirname

from .personal_settings import MY_SECRET_KEY, MY_ALLOWED_HOSTS, MY_DEBUG_VALUE

BASE_DIR =      dirname(dirname(__file__))
TEMPLATE_PATH = join(BASE_DIR, 'templates')
STATIC_PATH =   join(BASE_DIR, 'static')
DATABASE_PATH = join(BASE_DIR, 'portfolio.db')

SECRET_KEY = MY_SECRET_KEY
ALLOWED_HOSTS = MY_ALLOWED_HOSTS
DEBUG = MY_DEBUG_VALUE

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'projects',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'Portfolio.urls'

WSGI_APPLICATION = 'Portfolio.wsgi.application'


# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': DATABASE_PATH,
    }
}

# Templates
OPTIONS = {
        'context_processors' : [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        'debug' : MY_DEBUG_VALUE,
}

TEMPLATES = [
    {
        'BACKEND' : 'django.template.backends.django.DjangoTemplates',
        'DIRS' : [TEMPLATE_PATH],
        'APP_DIRS': True,
        'OPTIONS': OPTIONS
    },
]

# Internationalization

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'
STATIC_ROOT = join(dirname(BASE_DIR), 'public/static')
STATICFILES_DIRS = (STATIC_PATH,)
