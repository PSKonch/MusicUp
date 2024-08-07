from django.urls import path

from . import views

urlpatterns = [
    path("", views.login_user, name="user"),
    #path("user_creation", views.create_user_view, name="register")
]