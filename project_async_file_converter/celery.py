import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_async_file_converter.settings')

app = Celery('project_async_file_converter')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
