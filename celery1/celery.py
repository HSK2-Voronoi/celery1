import os

from celery import Celery
# from celery.schedule import crontab

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celery1.settings')

app = Celery('celery1')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'every-15-seconds' : {
        'task': 'email_celery.tasks.send_email_task',
        'schedule': 15,
        # 'schedule': crontab(15), 
        'args':('hsk2@voronoi.io',)
    }
}

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')