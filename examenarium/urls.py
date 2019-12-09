from django.urls import path, include
from django.contrib import admin
import main.views

admin.autodiscover()

urlpatterns = [
    path("", main.views.index, name="index"),
    path("media/", include('media.urls')),
    path("account/", include('main.urls')),
    path("time/", include('swingtime.urls')),
    path("homework/", include('homework.urls')),
    path("admin/", admin.site.urls),
]
