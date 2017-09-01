from .base import *

SECRET_KEY = 'development'

DEBUG = True

ALLOWED_HOSTS = []

try:
    from .local import *
except ImportError:
    pass
