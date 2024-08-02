from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("Artists/", views.Artists, name="artists"),
    path("News/", views.News, name="news")
]
