from django.db import models
from django.urls import reverse

# Create your models here.
class Artist(models.Model):

    nick_name = models.CharField((""), max_length=50)
    password = models.CharField((""), max_length=50)
    
    email = models.EmailField((""), max_length=254)

    #artist_post = models.ForeignKey("Post.Model", verbose_name=("art_post"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Artist")
        verbose_name_plural = ("Artists")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})

class Post(models.Model):

    

    class Meta:
        verbose_name = ("")
        verbose_name_plural = ("s")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
