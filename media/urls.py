from django.urls import path

from media import views

urlpatterns = [
    path("media/videos/", views.videos, name="videos"),
    path("media/images/", views.images, name="images"),
    path("dirs/", views.dirs, name="dirs"),
]