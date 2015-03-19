DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'websitedb',
        'USER': 'website1',
        'PASSWORD': 'university023',
        'HOST': 'localhost',
        'PORT': '',
        }
    }

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

EMAIL_HOST_USER = '***REMOVED***'
EMAIL_HOST_PASSWORD = '***REMOVED***'
