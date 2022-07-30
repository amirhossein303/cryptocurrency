CELERY_IMPORTS = 'config.tasks'

CELERY_BEAT_SCHEDULE = {
    'update-cryptocurrencies-data':{
        'task': 'update-cryptocurrencies-data',
        'schedule': 10, # each 10 seconds
    }
}

CELERY_RESULT_BACKEND = 'redis://redis:6379/2'
CELERY_BROKER_URL = 'amqp://guest:guest@rabbitmq:5672/'