from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from datetime import datetime


def index(request):
    d = str(datetime.now())
    return HttpResponse("Hello, world. You're at the home index at " + d)
