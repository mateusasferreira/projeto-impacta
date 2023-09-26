from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("registration/", views.registration, name="registration"),
    path("signup/", views.create_user, name="signup"),
]