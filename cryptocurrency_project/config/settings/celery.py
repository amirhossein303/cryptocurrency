CELERY_IMPORTS = 'config.tasks'

CELERYBEAT_SCHEDULE = {
    'update-cryptocurrencies-data':{
        'task': 'update-cryptocurrencies-data',
        'schedule': 10, # each 10 seconds
    }
}

CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/2'
CELERY_BROKER_URL = 'amqp://127.0.0.1:5672/'