import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'sAdfogkeWDFV2-94XVa1SDsdk0GSkvnrjf-alvngspoemvh'
    CELERY_BROKER_URL = 'amqp://localhost//'
