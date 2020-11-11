from celery import shared_task
from time import sleep
from django.core.mail import send_mail


@shared_task
def send_email_task(email):
    sleep(3)
    print(f'Got a periodic tasks with{email}')
    send_mail(
        'Celery Task Worked!', 
        'this is proof the task worked!',
        'viewofsunset@gmail.com',
        ['hsk@voronoi.io'],
        fail_silently=False
    )
    return None