from django.shortcuts import render
from django.http import HttpResponse
from .tasks import sleepy


# to activate @shared_task, add ".delay" at the end of function

def index(request):
    sleepy.delay(5)
    return HttpResponse('<h2> seond task is done!</h2>')