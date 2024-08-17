from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


from .models import CustomUser, Post_News, Song, Album
from django.contrib.auth.decorators import login_required
from .forms import LoadMusicForm, PostCreateForm

pages = {
    
}

# Create your views here.
def index(request): #То же самое, что News
    queryset = Post_News.objects.all()
    return render(request, "Music_Up_Dev/index.html", {'content': queryset })



def Artists_view(request):
    queryset = CustomUser.objects.all()
    return render(request, "Music_Up_Dev/artists.html", {'content': queryset})



def Posts_view(request):
    queryset = Post_News.objects.all()
    return render(request, "Music_Up_Dev/posts.html", {'content': queryset})


@login_required
def Songs_view(request):
    songs = Song.objects.all()
    return render(request, 'Music_Up_Dev/song_list.html', {'songs': songs})



@login_required
def Load_a_Song(request):
    
    if request.method == 'POST':
        form = LoadMusicForm(request.POST, request.FILES, user=request.user)
        
        if form.is_valid(): 
            form.save()
            return HttpResponseRedirect(reverse('song_list'))
        
    else:
        form = LoadMusicForm(user=request.user)
    return render(request, 'Music_Up_Dev/load_song.html', {'form': form})




@login_required
def Create_a_Post(request):

    author = request.user  

    if request.method == 'POST':
        form = PostCreateForm(request.POST)
        
        if form.is_valid():

            Post_News.objects.create(**form.cleaned_data, author=author)
            return HttpResponseRedirect(reverse('posts'))

    else:
        form = PostCreateForm()
    
    return render(request, "Music_Up_Dev/create_post.html", {'form': form})


def Create_a_News(request):
    return HttpResponse('Create a News')