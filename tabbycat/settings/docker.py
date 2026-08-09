# ==============================================================================
# Docker
# ==============================================================================

import os

ALLOWED_HOSTS = ["*"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_DB', 'tabbycat_2w63'),
        'USER': os.environ.get('POSTGRES_USER', 'tabbycat_2w63_user'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD', 'vDH1ZvccgVrqhjbaJ5YbDQh8wOCbnEbn'),
        'HOST': os.environ.get('POSTGRES_HOST', 'dpg-d9s5ifn40ujc73clc0ug-a'),
        'PORT': int(os.environ.get('POSTGRES_PORT', '5432')),
    }
}

if bool(int(os.environ['DOCKER_REDIS'])) if 'DOCKER_REDIS' in os.environ else False:
    CACHES = {
        "default": {
            "BACKEND": "django_redis.cache.RedisCache",
            "LOCATION": "redis://redis:6379/1",
            "OPTIONS": {
                "CLIENT_CLASS": "django_redis.client.DefaultClient",
                "SOCKET_CONNECT_TIMEOUT": 5,
                "SOCKET_TIMEOUT": 60,
            },
        },
    }

    CHANNEL_LAYERS = {
        "default": {
            "BACKEND": "channels_redis.core.RedisChannelLayer",
            "CONFIG": {
                "hosts": [("redis", 6379)],
                "group_expiry": 10800,
            },
        },
    }
