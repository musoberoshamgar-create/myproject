# ==============================================================================
# Github CI
# ==============================================================================

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

