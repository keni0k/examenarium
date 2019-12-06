from django.shortcuts import render
from .models import *


def videos(request):
    videos = Video.objects.filter(is_active=True)


def images(request):
    pass


def dirs(request):
    pass
