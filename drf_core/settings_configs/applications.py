# Application definition

PREINSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

PROJECT_APPS = [
    'rest_framework',
    'assets',
    'employee',
    'drf_yasg',
]

INSTALLED_APPS = PREINSTALLED_APPS + PROJECT_APPS
