from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils import timezone


class CustomUser(models.Model):
    is_artist = models.BooleanField(default=True)
    is_editor = models.BooleanField(default=True)
    
    user_email = models.EmailField(max_length=254)
    user_password = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.user_email

class Artist(CustomUser):
    
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='', blank=True)
    
    def __str__(self) -> str:
        return self.user_name

class Editor(CustomUser):
    
    def __str__(self) -> str:
        return self.user_name

class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album_title = models.CharField(max_length=300, blank=False)
    genre = models.CharField(max_length=100, blank=False)
    album_logo = models.ImageField()

    def __str__(self):
        return self.album_title + '-' + self.artist
    
class Song(models.Model):
   album = models.ForeignKey(Album, on_delete=models.CASCADE)
   song_title = models.CharField(max_length=250)
   is_favorite = models.BooleanField(default=False)
   file = models.FileField(upload_to='')

   def __str__(self):
       return self.song_title
   
class Post_News(models.Model):
    title = models.CharField(max_length=200, blank=True)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=timezone.now)
   
class Post(Post_News):
    author = models.ForeignKey(Artist, on_delete=models.CASCADE)
    
class News(Post_News):
    author = models.ForeignKey(Editor, on_delete=models.CASCADE)
    
