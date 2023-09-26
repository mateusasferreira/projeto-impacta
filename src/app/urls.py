from django.urls import path
from django.contrib.auth.views import LogoutView

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("registration/", views.registration, name="registration"),
    path("login/", views.signin, name="login"),
    path("logout/", LogoutView.as_view(), name="logout")
]