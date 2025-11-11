# settings.py (cleaned)

from pathlib import Path
import os
from dotenv import load_dotenv
from mongoengine import connect

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")  # loads .env next to manage.py

# ---- Core ----------------------------------------------------
SECRET_KEY = os.getenv("SECRET_KEY")
DEBUG = os.getenv("DEBUG", "False") == "True"

ALLOWED_HOSTS = ['*']

# ---- Apps & Middleware --------------------------------------
INSTALLED_APPS = [
    "blog",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "my_site.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        # Tip: APP_DIRS=True already picks up blog/templates/blog.
        # Keep this if you also have project-level templates:
        "DIRS": [BASE_DIR / "my_site" / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "my_site.wsgi.application"

# ---- Databases ----------------------------------------------
# Django’s internal tables (admin/auth) stay on SQLite:
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# MongoDB Atlas for your app data via MongoEngine:
MONGODB_URI = os.getenv("MONGODB_URI")
if MONGODB_URI:
    connect(host=MONGODB_URI, alias="default")
else:
    # Don’t print in production; log if desired.
    pass

# ---- Static / Media -----------------------------------------
STATIC_URL = "/static/"
STATICFILES_DIRS = [
    BASE_DIR / "blog" / "static",        
    BASE_DIR / "my_site" / "static",
]
STATIC_ROOT = BASE_DIR / "staticfiles"

# Django 5+ preferred way to set WhiteNoise storage
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# User uploads (if you have ImageField/FileField)
MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"

# ---- Misc ----------------------------------------------------
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# If behind a proxy/Render, ensure HTTPS detection:
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
