from django import forms
from user.models import CustomUser

class PostCreateForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField()