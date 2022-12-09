from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-(8^mv$!=-j+1n@3_p%i=o!lzg=1r68f_6s-eso$en4@fd93_=t"


# Application definition

INSTALLED_APPS = [
    "csv_to_db",
]


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

USE_TZ = False

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
