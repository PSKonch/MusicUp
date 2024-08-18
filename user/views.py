from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import get_user, get_user_model, authenticate, login, logout
from django.urls import reverse, reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import LoginUserForm, CreateUserForm, UserPasswordChangeForm
from .models import CustomUser
from django.views.decorators.cache import never_cache

# Create your views here.

class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'user/login.html'
    extra_context = {'title': 'Авторизация'}
    
    def get_success_url(self):
        return reverse_lazy('index')


'''
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
'''


def create_user_view(request):
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        
        if form.is_valid():
            cd = form.cleaned_data
            user = form.save()
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        
    else: form = CreateUserForm()
    
    return render(request, 'user/user_creation.html', {'form': form})
        
        
        
def logout_user(request):
   logout(request)
   return HttpResponseRedirect(reverse('login'))



def change_password(request):
    
    if request.method == 'POST':
        form = UserPasswordChangeForm(user=request.user, data=request.POST)

        if form.is_valid():
            cd = form.cleaned_data
        
            if form.user.check_password(cd['old_password']) and (cd['new_password1'] == cd['new_password2']):
                form.user.set_password(cd['new_password1'])
                form.user.save()
                return redirect('/')
            
    else: form = UserPasswordChangeForm(user=request.user)
        
    return render(request, 'user/change_password.html', {'form': form})


@login_required
def UserProfile(request):
    # Всегда обновляем `queryset` для текущего пользователя
    queryset = get_object_or_404(CustomUser, username=request.user.username)
    
    context = {'queryset': queryset}
    return render(request, 'user/profile.html', context)

