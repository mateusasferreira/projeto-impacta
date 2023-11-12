from django.urls import path
from django.contrib.auth.views import LogoutView

from . import views

urlpatterns = [
    path("", views.UsersList.as_view(), name="index"),
    path("registration/", views.RegistrationView.as_view(), name="registration"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("users/", views.UsersList.as_view(), name="user-details"),
    path("users/<int:id>", views.user_details, name="user-details"),
    path("users/<int:id>/message", views.user_message, name="user_message"),
    path("messages/<int:id>/delete", views.delete_message, name="delete_message")
]