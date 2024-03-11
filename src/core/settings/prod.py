from .base import *
import os

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': os.getenv('DB_HOST'),
        'NAME': os.getenv('DB_NAME'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'USER': os.getenv('DB_USER'),
        'PORT': os.getenv('DB_PORT'),
    },
}