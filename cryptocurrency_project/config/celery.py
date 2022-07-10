import os

from celery import Celery
from decouple import config


CELERY_MAIN_NAME = config('CELERY_MAIN_NAME')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.local')
app = Celery(CELERY_MAIN_NAME)
app.config_from_object('django.conf:settings')