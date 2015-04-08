import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', 
        'NAME': os.environ['NAME'],
        'USER': os.environ['USER'],
        'PASSWORD': os.environ['PASSWORD'],
        'HOST': 'localhost',
        'PORT': '',
        }
    }

EMAIL_HOST = os.environ['EMAIL_HOST']
EMAIL_PORT = os.environ['EMAIL_PORT']
EMAIL_USE_TLS = True

EMAIL_HOST_USER = os.environ['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']
