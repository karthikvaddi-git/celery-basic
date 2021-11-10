from django.shortcuts import render
from django.http import HttpResponse
from .task import test_func
# Create your views here.
from send_mail_app.task import send_mail_func

def home(request):

    test_func.delay()
    return HttpResponse('hello world')

def send_mail_all(request):
    send_mail_func.delay()
    return HttpResponse('done sent mail')
