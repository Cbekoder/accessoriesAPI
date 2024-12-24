from .settings import *  # noqa

###################################################################
# General
###################################################################

DEBUG = False

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "accessories_store",
        "USER": "postgres",
        "PASSWORD": "parol12345",
        "HOST": "db",
        "PORT": "5432",
        "ATOMIC_REQUESTS": False,
    }
}

###################################################################
# Django security
###################################################################

# https://docs.djangoproject.com/en/5.1/ref/settings/#use-x-forwarded-host
# https://docs.djangoproject.com/en/5.1/ref/settings/#secure-proxy-ssl-header
USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# https://docs.djangoproject.com/en/5.1/ref/settings/#csrf-cookie-secure
# https://docs.djangoproject.com/en/5.1/ref/settings/#csrf-trusted-origins
CSRF_COOKIE_SECURE = True  # if True, CSRF Cookie will work only on HTTPS
CSRF_TRUSTED_ORIGINS = [
    "https://javohir.fassco.uz",
]

###################################################################
# CORS
###################################################################

CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_HEADERS = ["*"]
