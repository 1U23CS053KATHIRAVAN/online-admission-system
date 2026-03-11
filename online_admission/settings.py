from pathlib import Path
import os

# =========================
# BASE DIRECTORY
# =========================
BASE_DIR = Path(__file__).resolve().parent.parent


# =========================
# SECURITY SETTINGS
# =========================
SECRET_KEY = os.environ.get(
    'DJANGO_SECRET_KEY',
    'django-insecure-change-this-key'
)

DEBUG = True

ALLOWED_HOSTS = ['online-admission-system.onrender.com']


# =========================
# APPLICATIONS
# =========================
INSTALLED_APPS = [

    # Modern Admin UI
    "jazzmin",

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Your App
    'admission',
]


# =========================
# MIDDLEWARE
# =========================
MIDDLEWARE = [

    'django.middleware.security.SecurityMiddleware',

    # WhiteNoise for static files
    'whitenoise.middleware.WhiteNoiseMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# =========================
# URL CONFIG
# =========================
ROOT_URLCONF = 'online_admission.urls'


# =========================
# TEMPLATES
# =========================
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',

        'DIRS': [BASE_DIR / 'templates'],

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


# =========================
# WSGI
# =========================
WSGI_APPLICATION = 'online_admission.wsgi.application'


# =========================
# DATABASE
# =========================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# =========================
# PASSWORD VALIDATION
# =========================
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {'min_length': 8}
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# =========================
# INTERNATIONALIZATION
# =========================
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True
USE_TZ = True


# =========================
# STATIC FILES
# =========================
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

STATIC_ROOT = BASE_DIR / 'staticfiles'

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# =========================
# MEDIA FILES
# =========================
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


# =========================
# AUTH REDIRECT SETTINGS
# =========================
LOGIN_URL = 'admission:login'
LOGIN_REDIRECT_URL = 'admission:student_dashboard'
LOGOUT_REDIRECT_URL = 'admission:home'


# =========================
# EMAIL SETTINGS
# =========================
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DEFAULT_FROM_EMAIL = 'admin@admission.com'


# =========================
# DEFAULT PRIMARY KEY
# =========================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# =========================
# JAZZMIN ADMIN THEME
# =========================
JAZZMIN_SETTINGS = {

    "site_title": "Admission Admin",

    "site_header": "Online Admission Management System",

    "site_brand": "Admission Portal",

    # Logo
    "site_logo": "img/logo2.png",
    "login_logo": "img/logo2.png",

    # Round Logo Style
    "site_logo_classes": "img-circle",

    # Browser Tab Icon
    "site_icon": "img/favicon.ico",

    "welcome_sign": "Welcome to the Admission Dashboard",

    "copyright": "Admission System 2026",

    "search_model": ["auth.User", "admission.Student"],

    "topmenu_links": [
        {"name": "Dashboard", "url": "admin:index"},
        {"model": "admission.Student"},
        {"model": "admission.Course"},
    ],

    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",

        "admission.Student": "fas fa-user-graduate",
        "admission.Course": "fas fa-book",
    },

    "show_sidebar": True,

    "navigation_expanded": True,

    "order_with_respect_to": ["admission", "auth"],

    # Modern Theme
    "theme": "superhero",

    # Dark Mode Theme
    "dark_mode_theme": "cyborg",
}