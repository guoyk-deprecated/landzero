import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '0m@6y1**t&22qp14qx+37oyhorofl$p%q)%*#_u0)1)qa8j63%'

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

CACHES = {
    'default': {
        'BACKEND': 'redis_cache.RedisCache',
        'LOCATION': 'localhost:6379',
    },
}

CELERY_BROKER_URL = 'redis://localhost:6379/0'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

WEIXIN_MP = {
    'ORG_ID': '',
    'APP_ID': '',
    'APP_SECRET': '',
    'APP_TOKEN': '',
    'APP_AES_KEY': '',
}
