from celery import Celery
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'converter_celery_redis')
app = Celery('convert', broker='redis://localhost:8000/0',backend='redis://localhost')
# app.conf.broker_url('redis://localhost:6379/0')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
