from django.urls import path 
from email_celery.views import * 

urlpatterns = [
    path('', index, name='index'),
]