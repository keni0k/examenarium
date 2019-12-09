from django.urls import path
from django.contrib import admin
from django.contrib import auth
import main.views
import media.views
import swingtime.views
from django.contrib.auth.views import LoginView, LogoutView

from examenarium import settings

admin.autodiscover()

urlpatterns = [
    path("", main.views.index, name="index"),

    path("media/videos/", media.views.videos, name="videos"),
    path("media/images/", media.views.images, name="images"),
    path("dirs/", media.views.dirs, name="dirs"),

    path("login/", LoginView.as_view(), name='login'),
    path("register/", main.views.register, name="register"),
    path('logout/', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),

    path("accounts/profile/", main.views.profile, name="profile"),

    path("calendar/", swingtime.views.event_listing, name="calendar"),

    path("admin/", admin.site.urls),
]
