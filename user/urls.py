from django.urls import path
from django.contrib.auth.views import LogoutView

from . import views

urlpatterns = [
    path("login", views.LoginUser.as_view(), name="login"),
    path("register", views.create_user_view, name="register"),
    path("logout", views.logout_user, name="logout"), 
    path("change_password", views.change_password, name="change_password")
]