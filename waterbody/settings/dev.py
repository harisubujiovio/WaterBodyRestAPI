from .common import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

SECRET_KEY = 'django-insecure-_u!9^96h_4a5#=-0vg7!w4oynse%0ql9!iqy9)08w^yruap15i'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'WaterBodyAdmin',
        'USER': 'postgres',
        'PASSWORD': '78fghAsd',
        'HOST': '127.0.0.1',
        'PORT': '5432'
    }
}