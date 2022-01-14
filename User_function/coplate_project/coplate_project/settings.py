"""
Django settings for coplate_project project.

Generated by 'django-admin startproject' using Django 3.2.9.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import json
import os
from pathlib import Path

from django.core.exceptions import ImproperlyConfigured

BASE_DIR = Path(__file__).resolve().parent.parent

secret_file = os.path.join(BASE_DIR, 'secrets.json')  # secrets.json 파일 위치를 명시

with open(secret_file) as f:
    secrets = json.loads(f.read())


def get_secret(setting):
    """비밀 변수를 가져오거나 명시적 예외를 반환한다."""
    try:
        return secrets[setting]
    except KeyError:
        error_msg = "Set the {} environment variable".format(setting)
        raise ImproperlyConfigured(error_msg)


SECRET_KEY = get_secret("SECRET_KEY")
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'coplate',
    'widget_tweaks',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
]

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]
SITE_ID = 1
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'coplate_project.urls'

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

WSGI_APPLICATION = 'coplate_project.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "coplate.validators.CustomPasswordValidator",
    }
]

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'ko'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "/static/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/uploads/"
# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'coplate.User'
ACCOUNT_SIGNUP_REDIRECT_URL = 'index'
LOGIN_REDIRECT_URL = 'index'
LOGIN_URL = "account_login"  # 웹 서비스에서 사용하는 로그인에 대한 URL을 설정 [ allauth 를 사용 중이여서 이렇게 설정 ]
# [ 로그인이 되어 있지 않을 경우 해당 URL로 이동 ]
ACCOUNT_LOGOUT_ON_GET = True
# ACCOUNT_AUTHENTICATION_METHOD = "username_email"
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_SIGNUP_FORM_CLASS = 'coplate.forms.SignupForm'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_PASSWORD_INPUT_RENDER_VALUE = True  # 비밀번호 form이 지워지는 것을 방지
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = "account_email_confirmation_done"
# 로그인한 사용자가 이메일 인증을 했을 때 렌더할 템플릿 네임
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = "account_email_confirmation_done"
# 로그인 하지 않은 사용자가 이메일 인증을 했을때 렌더할 템플릿 네임임
# PASSWORD_RESET_TIMOUT = (단위: 초) 패스워드 변경 및 찾기의 유효 url 시간
ACCOUNT_EMAIL_SUBJECT_PREFIX = ""
# Account email 의 앞부분을 빈 문자열로 만들어주는 설정
# allauth 가 발송하는 이메일제목은 웹사이트의 도메인이 앞에 붙게 되는데 그것을 제거해주는 역활


# Email settings
# allauth 가 제공하는 이메일 인증이나 비밀번호 찾기 기능을 활용하려면 이메일을 보낼 수 있어야 하는데 이때, 이메일을 어떻게 보내야할지 설정하는게
# EMAIL_BACKEND 기능입니다. 지금 설정값은 터미널 콘솔로 이메일을 보내게 설정해둔것 입니다. [ 나중에 변경 예정 ]
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
