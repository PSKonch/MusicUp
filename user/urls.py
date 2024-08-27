from django.urls import path
from django.contrib.auth.views import LogoutView, PasswordResetView, PasswordResetConfirmView, PasswordResetCompleteView

from . import views

urlpatterns = [
    path("login", views.LoginUser.as_view(), name="login"),
    path("register", views.create_user_view, name="register"),
    path("logout", views.logout_user, name="logout"), 
    path("change_password", views.change_password, name="change_password"),
    path("profile", views.UserProfile, name="profile"),
    path('password-reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset/complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]