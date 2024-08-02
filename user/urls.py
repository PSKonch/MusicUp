from django.urls import path

from . import views

urls = [
    path("", views.login, name="user")
]