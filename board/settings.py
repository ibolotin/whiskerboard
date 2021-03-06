import os

PROJECT_ROOT = os.path.dirname(__file__)

######################################
# Main
######################################

DEBUG = True
ROOT_URLCONF = 'board.urls'
SITE_ID = 1

# Missing by Default. Add your own unique key.
SECRET_KEY = ";wouvjsmle,mvu8shdnflgklrhofdgw;eodivuqok@$TWVE#$5gvw45^@VR@B"

######################################
# Apps
######################################

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'board',
    'colorfield',
    'tastypie',
    'randomslugfield',
    'waffle'
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'waffle.middleware.WaffleMiddleware',
)

######################################
# Database
######################################

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'whisker',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'USER': 'whisker',
        'PASSWORD': 'board',
        }}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': 'whiskerboard.sqlite3',
#         'USER': '',
#         'PASSWORD': '',
#         'HOST': '',
#         'PORT': '',
#     }
# }

######################################
# Localisation
######################################

TIME_ZONE = 'UTC'
LANGUAGE_CODE = 'en-US'
USE_I18N = True
USE_L10N = True


######################################
# Logging
######################################

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}


######################################
# Media/Static
######################################

MEDIA_ROOT = ''
MEDIA_URL = ''

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'collected_static')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

######################################
# Templates
######################################

TEMPLATE_DEBUG = DEBUG

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    'django.core.context_processors.request',
    "django.contrib.messages.context_processors.messages",
    'board.context_processors.current_site',
)

BUGZILLA_URL = 'https://bugzilla.mozilla.org'
BUGZILLA_PRODUCT = 'Mozilla Services'
BUGZILLA_COMPONENT = 'Operations'
BUGZILLA_USERNAME = None
BUGZILLA_PASSWORD = None
