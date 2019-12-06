from django.urls import path
from django.contrib import admin
import main.views
import media.views
admin.autodiscover()

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", main.views.index, name="index"),

    path("media/videos/", media.views.videos, name="videos"),
    path("media/images/", media.views.images, name="images"),
    path("dirs/", media.views.dirs, name="dirs"),

    path("admin/", admin.site.urls),
]
