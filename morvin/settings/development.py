from .base import *

DEBUG = True


ALLOWED_HOSTS = ['127.0.0.1']



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'hall2',
    }
}
