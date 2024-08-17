from django.urls import path
from django.views.decorators.cache import cache_page

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("Artists/", views.Artists_view, name="artists"),
    path("CreatePost/", cache_page(5)(views.Create_a_Post), name="create_post"),
    path("Posts/", views.Posts_view, name="posts"),
    path("Songs/", cache_page(10)(views.Songs_view), name="song_list"),
    path("LoadSong/", views.Load_a_Song, name="load_song"),
]
