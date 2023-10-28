from django.urls import path
from django.contrib.auth.views import LogoutView

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("registration/", views.registration, name="registration"),
    path("login/", views.signin, name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("users/<int:id>", views.user_details, name="user-details"),
    path("users/<int:id>/message", views.user_message, name="user_message")
]