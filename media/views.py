from django.shortcuts import render
from .models import *


# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")


def videos(request):
    pass


def images(request):
    pass


def dirs(request):
    pass
