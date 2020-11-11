from django.shortcuts import render
from django.http import HttpResponse
from .tasks import *


# to activate @shared_task, add ".delay" at the end of function

# def index(request):
#     sleepy.delay(5)
#     return HttpResponse('<h2> seond task is done!</h2>')


def index(request):
    email = 'viewofsunset@naver.com'
    send_email_task.delay(email)
    return HttpResponse('<h2> email has been sent 2!</h2>')