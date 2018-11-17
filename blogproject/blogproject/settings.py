"""
Django settings for blogproject project.

Generated by 'django-admin startproject' using Django 2.0.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

print('BASE_DIR', BASE_DIR)
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '7a9ddkbv6(yw+z+oy6^++nwvg6rwi9a24h@^8%5()+^fcsjps)'

# SECURITY WARNING: don't run with debug turned on in production!
# debug=False，django将不再加载静态文件
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
    'blog'
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

ROOT_URLCONF = 'blogproject.urls'

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

WSGI_APPLICATION = 'blogproject.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.mysql',
    # 数据库名称
    #     'NAME': 'blogproject',
    #     'USER':'root',
    #     'PASSWORD':'shange',
    #     'HOST':'127.0.0.1',
    #    'PORT':'3306'
    # }
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        # 数据库名称
        'NAME': 'blog',
        'USER': 'root',
        'PASSWORD': 'Root!!2018',
        'HOST': '127.0.0.1',
        'PORT': '3306'
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True
# 为False表示当前项目是不分时区的,为True是按utc时区
USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/
# 加载尼玛啊,STATIC_ROOT只是django收集静态文件的路径,
mystatic_path = os.path.join(BASE_DIR,"collect_static/static")

#STATIC_ROOT = mystatic_path
# url是访问路径的前缀，可以设置访问路径
#这个如果为/居然优先级比urls里的配置高，如果为/就会覆盖urls里的配置路径
STATIC_URL = '/static/'
#
STATICFILES_DIRS = [
	mystatic_path
]

#print('STATIC_ROOT', STATIC_ROOT)

# 这个路径对应img的上传到哪儿个文件夹下,是绝对路径
MEDIA_ROOT = os.path.join(mystatic_path, 'submit')
#print('MEDIA_ROOT', MEDIA_ROOT)
# 这个url对应imgField返回的url路径的前缀,可以随便写,其实跟webpack的publicPath是一样的
MEDIA_URL = '/static/submit/'
# 添加这个用于打印执行的sql语句
# LOGGING = {
#   'version': 1,
#  'disable_existing_loggers': False,
#    'handlers': {
#        'console': {
#            'class': 'logging.StreamHandler',
#       },
#   },
#   'loggers': {
#        'django.db.backends': {
#           'handlers': ['console'],
#          'level': 'DEBUG' if DEBUG else 'INFO',
#       },
#    },
# }


# 跨域增加忽略
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True
# 跨域允许的网站
CORS_ORIGIN_WHITELIST = (
    '*'
)
# 跨域允许的方法
CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
    'VIEW',
)
# 跨域允许的请求头
CORS_ALLOW_HEADERS = (
    'XMLHttpRequest',
    'X_FILENAME',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
)
