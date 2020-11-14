from .base import *  # NOQA

import dj_database_url


APP_ENV = "dev"
APP_VERSION = "dev"
SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]
DEBUG = True

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS += ["modules.core"]

DATABASES = {
    "default": dj_database_url.config(default=os.environ["DJANGO_DATABASE_URL"])
}

# Internalization settings

TIME_ZONE = os.environ.get("TIME_ZONE", "UTC")
