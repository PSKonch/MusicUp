from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.
class CustomUser(AbstractUser):
    is_artist = models.BooleanField(default=True)
    is_editor = models.BooleanField(default=False)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='', blank=True)
    
    def __str__(self) -> str:
        return self.email