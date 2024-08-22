from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import get_user_model
from user.models import CustomUser


class LoginUserForm(AuthenticationForm):
    
    class Meta:
        model = get_user_model()
        fields = ('username', 'password')

    
class CreateUserForm(UserCreationForm):
    
    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'description', 'image')
        
class UserPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField()
    new_password1 = forms.CharField()
    new_password2 = forms.CharField()