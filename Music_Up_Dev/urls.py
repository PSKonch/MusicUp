from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("Artists/", views.Artists_view, name="artists"),
]
