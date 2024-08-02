from django import forms

class LoginUserForm(forms.Form):
    username = forms.CharField(label="login", widget=forms.TextInput(attrs={'class': 'form-input'}), max_length=100, required=False)
    password = forms.CharField(label="password", widget=forms.PasswordInput(attrs={'class': 'form-input'}), max_length=100, required=False)