from .base import *

DEBUG = True


ALLOWED_HOSTS = ['localhost']



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'hall2',
    }
}
