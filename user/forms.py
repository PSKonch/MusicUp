from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from user.models import CustomUser


class LoginUserForm(AuthenticationForm):
    
    class Meta:
        model = get_user_model()
        fields = ('username', 'password')

    
class CreateUserForm(UserCreationForm):
    
    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'description', 'image')