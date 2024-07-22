from django.db import models
from django.urls import reverse

# Create your models here.
class Post(models.Model):

    post_name = models.CharField(max_length=50, blank=False)
    is_published = models.BooleanField()

    class Meta:
        verbose_name = ("Post")
        verbose_name_plural = ("Posts")

    def __str__(self):
        return self.post_name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})



class Artist(models.Model):

    nick_name = models.CharField(max_length=50, blank=False)
    password = models.CharField(max_length=50, blank=False)
    
    email = models.EmailField(max_length=254, blank=False)

    artist_post = models.ForeignKey(Post, verbose_name=("art_post"), on_delete=models.CASCADE, blank=True)

    class Meta:
        verbose_name = ("Artist")
        verbose_name_plural = ("Artists")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
    