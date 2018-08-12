from .base import *

with open(os.path.join(BASE_DIR, 'deploy', 'django-secret-key.txt')) as f:
    SECRET_KEY = f.read().strip()

DEBUG = False

ALLOWED_HOSTS = ['*']

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Media files storage
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_STORAGE_BUCKET_NAME = 'lazydevelo'
with open(os.path.join(BASE_DIR, 'deploy', 'aws-access-key-id.txt')) as f:
    AWS_ACCESS_KEY_ID = f.read().strip()
with open(os.path.join(BASE_DIR, 'deploy', 'aws-secret-access-key.txt')) as f:
    AWS_SECRET_ACCESS_KEY = f.read().strip()
MEDIA_URL = 'https://{}.s3.amazonaws.com/media/'.format(AWS_STORAGE_BUCKET_NAME)

try:
    from .local import *
except ImportError:
    pass
