from .settings import *

INSTALLED_APPS = [
    "corsheaders",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_filters",
    "rest_framework",
    "rest_framework_simplejwt",
    "apps.health",
    "apps.programmes",
    "apps.degrees",
    "apps.learning_outcomes",
    "apps.lib",
    "apps.courses",
    "apps.users",
    "apps.study_plans",
]

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
