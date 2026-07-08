import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# NOT: Canlıya alırken bunu Render'da environment variable olarak tanımlaman daha güvenli olur
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-degistir-bunu-render-ortam-degiskeninde')

DEBUG = False
ALLOWED_HOSTS = ['*']

ROOT_URLCONF = 'davetiye_proj.urls'

INSTALLED_APPS = [
    'django.contrib.staticfiles',
    'davetiye_app',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.common.CommonMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'davetiye_proj.wsgi.application'

# Bu sitede kullanıcıdan veri toplanmıyor (sadece davetiye gösteriliyor),
# bu yüzden gerçek bir veritabanına ihtiyaç yok. Django'nun çalışması için
# yine de minik bir sqlite tanımlıyoruz, hiç kullanılmayacak.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

LANGUAGE_CODE = 'tr'
TIME_ZONE = 'Europe/Istanbul'
USE_I18N = True
USE_TZ = True

# --- Statik dosyalar (CSS/font/ses) ---
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
