from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("Artists/", views.Artists_view, name="artists"),
    path("CreatePost/", views.Create_a_Post, name="create_post"),
    path("Posts/", views.Posts_view, name="posts")
]
