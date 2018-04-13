from .base import *

SECRET_KEY = 'development'

DEBUG = True

ALLOWED_HOSTS = []

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

try:
    from .local import *
except ImportError:
    pass
