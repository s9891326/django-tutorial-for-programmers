from .base import *

SECRET_KEY = 'django-insecure-as$m8ve_#1ms@)wan9o@fr-o1fz4xl+&gv3ab11z1&*jg4@888'
DEBUG = True
TEMPLATE_DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

