from .base import *

with open(os.path.join(BASE_DIR, 'deploy', 'django-secret-key.txt')) as secret_key_file:
    SECRET_KEY = secret_key_file.read().strip()

DEBUG = False

ALLOWED_HOSTS = ['*']

try:
    from .local import *
except ImportError:
    pass
