from django.db import models
from django.urls import reverse
from django.utils import timezone
from user.models import Artist, Editor, CustomUser

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
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    
class News(Post_News):
    author = models.ForeignKey(Editor, on_delete=models.CASCADE)
    
