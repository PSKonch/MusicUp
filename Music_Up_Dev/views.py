from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import CustomUser, News, Artist, Post, Post_News, Song, Album
from django.contrib.auth.decorators import login_required
from .forms import PostCreateForm

# Create your views here.
def index(request): #То же самое, что News
    queryset = News.objects.all()
    return render(request, "Music_Up_Dev/index.html", {'content': queryset })



def Artists_view(request):
    queryset = CustomUser.objects.all()
    return render(request, "Music_Up_Dev/artists.html", {'content': queryset})



def Posts_view(request):
    queryset = Post_News.objects.all()
    return render(request, "Music_Up_Dev/posts.html", {'content': queryset})



def Songs_view(request):
    return HttpResponse("Songs List")



@login_required
def Load_a_Song(request):
    return HttpResponse('Load a Song')



@login_required
def Create_a_Post(request):

    if request.method == 'POST':
        form = PostCreateForm(request.POST)
        
        if form.is_valid():
            
            try:
                Post_News.objects.create(**form.cleaned_data)
                return HttpResponseRedirect(reverse('posts'))
            
            except:
                form.add_error(None, "Ошибка оформления")
    else: form = PostCreateForm()
    
    return render(request, "Music_Up_Dev/create_post.html", {'form': form})


def Create_a_News(request):
    return HttpResponse('Create a News')