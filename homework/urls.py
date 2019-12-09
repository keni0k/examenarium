from django.urls import path
from homework.views import db

urlpatterns = [
    path("", db, name="homework"),
    ]
