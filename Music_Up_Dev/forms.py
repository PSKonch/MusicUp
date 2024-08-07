from urllib import request
from django import forms
from user.models import CustomUser
from django.contrib.auth import get_user, get_user_model
from .models import Song, Album

class PostCreateForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField()
    

class LoadMusicForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['album', 'song_title', 'is_favorite', 'file']
    
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(LoadMusicForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        song = super(LoadMusicForm, self).save(commit=False)
        song.artist = self.user
        if commit:
            song.save()
        return song