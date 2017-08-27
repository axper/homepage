import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

with open(os.path.join(BASE_DIR, 'deploy', 'django_secret_key.txt')) as secret_key_file:
    SECRET_KEY = secret_key_file.read().strip()

DEBUG = False

ALLOWED_HOSTS = ['*']
