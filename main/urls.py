from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from examenarium import settings
from main import views

urlpatterns = [
    path("login/", LoginView.as_view(), name='login'),
    path("register/", views.register, name="register"),
    path("logout/", LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
    path("profile/", views.profile, name="profile"),
]