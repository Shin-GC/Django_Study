"""
Django settings for podomarket_project project.

Generated by 'django-admin startproject' using Django 4.0.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import json
import os
from pathlib import Path
from django.core.exceptions import ImproperlyConfigured

BASE_DIR = Path(__file__).resolve().parent.parent

secret_file = os.path.join(BASE_DIR, 'secrets.json')

with open(secret_file) as f:
    secrets = json.loads(f.read())


def get_secret(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
        error_msg = "Set the {} environment variable".format(setting)
        raise ImproperlyConfigured(error_msg)


SECRET_KEY = get_secret("SECRET_KEY")
# Build paths inside the project like this: BASE_DIR / 'subdir'.

DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django_extensions',
    'podomarket',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # 만약 소셜로그인이 필요할 경우 allauth 문서 참조해서 추가하기
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

ROOT_URLCONF = 'podomarket_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'podomarket/templates/podomarket/../podomarket/templates']
        ,
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

WSGI_APPLICATION = 'podomarket_project.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'podomarket.validators.CustomPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'ko'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'podomarket.User'  # 사용할 모델

ACCOUNT_SIGNUP_REDIRECT_URL = 'index'  # 회원가입시 홈페이지로 리다이렉트 하기

LOGIN_REDIRECT_URL = 'index'  # 로그인시 바로 홈페이지로 리다이렉트 하기
ACCOUNT_LOGOUT_ON_GET = True  # 로그아웃시 확인창 안뜨고 바로 로그아웃 가능하게

ACCOUNT_SIGNUP_FORM_CLASS = 'podomarket.forms.SignupForm'  # 새로 만든 Form을 회원가입시 나오게 하기 위해 추가

ACCOUNT_CONFIRM_EMAIL_ON_GET = True  # 이메일 인증 링크를 누르면 바로 인증이 완료되게하기
ACCOUNT_AUTHENTICATION_METHOD = 'email'  # 로그인시 username 이 아니라 email을 사용하게 하는 설정
ACCOUNT_EMAIL_REQUIRED = True  # 회원가입시 필수 이메일을 필수항목으로 만들기
# ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = "urls.py에서 설정한 이름"
# 유저가 인증을 완료했을때 연결할 URL
# ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = "urls.py 에서 설정한 이름"
# 로그인 하지 않은 사람이 인증을 했을때 연결할 URL
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = "account_email_confirmation_done"
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = "account_email_confirmation_done"

ACCOUNT_USERNAME_REQUIRED = False  # USERNAME 을 필수항목에서 제거
ACCOUNT_SESSION_REMEMBER = True  # 브라우저를 닫아도 세션기록 유지! [ 로그인 안풀리게 ! ]
# SESSION_COOKIE_AGE = 3600  # 쿠키를 한시간만 저장 [ 세션 ]
ACCOUNT_PASSWORD_INPUT_RENDER_VALUE = True  # 패스워드 입력이 사라지지 않게
# Email settings
# allauth가 제공하는 이메일 인증이나 비밀번호 찾기 기능을 활용하려면 이메일을 보낼 수 있어야 하는데 이때, 이메일을 어떻게 보내야할지 설정하는게
# EMAIL_BACKEND 기능입니다. 지금 설정값은 터미널 콘솔로 이메일을 보내게 설정해둔것 입니다. [ 나중에 변경 예정 ]
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
