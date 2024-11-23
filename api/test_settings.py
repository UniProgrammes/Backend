from .settings import *

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "test_db",
        "USER": "postgres",
        "PASSWORD": "postgres",
        "HOST": "test_db",
        "PORT": "5432",
    }
}
