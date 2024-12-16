"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 5.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""
from datetime import timedelta
from pathlib import Path

from django.conf.global_settings import STATICFILES_DIRS, STATIC_ROOT

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-#%7cr2(8ajvbrfgbo(&r)2#dm!w1pg&q**20a972ynb*ec@2%z'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_simplejwt',
    'drf_yasg',
    'corsheaders',
    'inventory',
    'main',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_HEADERS = ['*',]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES' : (
        'rest_framework.permissions.IsAuthenticated',
    )
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=5),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=10)
}

SWAGGER_SETTINGS = {
   'SECURITY_DEFINITIONS': {
      'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
      }
   }
}


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = "static/"
STATICFILES_DIRS = (BASE_DIR / "staticfiles",)
STATIC_ROOT = BASE_DIR / "static"

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


JAZZMIN_SETTINGS = {
    "site_title": "Accessories Warehouse Admin",

    "site_header": "Accessories Warehouse",

    "site_brand": "Warehouse",

    "site_logo": "warehouse/img/logo.png",

    "login_logo": None,

    "login_logo_dark": None,

    "site_logo_classes": "img-circle",

    "site_icon": "warehouse/img/favicon.ico",

    "welcome_sign": "Welcome to Accessories Warehouse System",

    "copyright": "Accessories Magazine Ltd",

    "search_model": ["auth.User", "warehouse.Product", "warehouse.Category"],

    "user_avatar": None,

    # Top Menu #
    "topmenu_links": [

        {"name": "Home",  "url": "admin:index", "permissions": ["auth.view_user"]},

        {"name": "Support", "url": "https://example.com/support", "new_window": True},

        {"model": "auth.User"},

        {"app": "warehouse"},
    ],

    # User Menu #

    "usermenu_links": [
        {"name": "Support", "url": "https://example.com/support", "new_window": True},
        {"model": "auth.user"}
    ],

    # Side Menu #

    "show_sidebar": True,

    "navigation_expanded": True,

    "hide_apps": [],

    "hide_models": [],

    "order_with_respect_to": ["auth", "warehouse", "warehouse.category", "warehouse.product"],

    "custom_links": {
        "warehouse": [{
            "name": "Stock Updates",
            "url": "stock_updates",
            "icon": "fas fa-boxes",
            "permissions": ["warehouse.view_product"]
        }]
    },

    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "warehouse": "fas fa-warehouse",
        "warehouse.product": "fas fa-box",
        "warehouse.category": "fas fa-tags",
    },
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",

    # Related Modal #
    "related_modal_active": False,

    # UI Tweaks #
    "custom_css": None,
    "custom_js": None,
    "use_google_fonts_cdn": True,
    "show_ui_builder": False,

    # Change view #
    "changeform_format": "horizontal_tabs",
    "changeform_format_overrides": {"auth.user": "collapsible", "warehouse.product": "vertical_tabs"},
    "language_chooser": False,
}

