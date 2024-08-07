from django import forms
from django.contrib.auth.forms import UserCreationForm

from user.models import CustomUser


class LoginUserForm(forms.Form):
    username = forms.CharField(label="login", widget=forms.TextInput(attrs={'class': 'form-input'}), max_length=100, required=False)
    password = forms.CharField(label="password", widget=forms.PasswordInput(attrs={'class': 'form-input'}), max_length=100, required=False)
    
class CreateUserForm(UserCreationForm):
    
    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'description', 'image')