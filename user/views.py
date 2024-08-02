from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import get_user, get_user_model, authenticate, login
from django.urls import reverse

from .forms import LoginUserForm

# Create your views here.


def login_user(request):
    
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            
            if user and user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
    
    else:
        form = LoginUserForm()
    
    return render(request, 'user/login.html', {'form' : form})
            
        
            
            
    form = LoginUserForm()
    return render(request, 'user/login.html', {'form': form})

def logout(request):
    return HttpResponse("Логаут")

