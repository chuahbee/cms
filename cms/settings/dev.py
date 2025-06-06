from .base import *
from decouple import config, Csv

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config(
    "DJANGO_SECRET_KEY",
    default="django-insecure-gk=5ywnzgrtffbfv^+liyawejd=0hp^fln99j72$#05k8zwn8y"
)

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = config(
    "DJANGO_ALLOWED_HOSTS",
    default="localhost,127.0.0.1",
    cast=Csv()
)

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# INSTALLED_APPS += ["portfolio"]  

try:
    from .local import *
except ImportError:
    pass
