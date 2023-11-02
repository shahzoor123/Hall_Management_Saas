from .base import *


DEBUG = True


ALLOWED_HOSTS = ['*','.vercel.app', '.now.sh']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '.././server_v2',
    }
}

