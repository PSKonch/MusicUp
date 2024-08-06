from django.shortcuts import render
from django.http import HttpResponse
from .models import CustomUser, News

# Create your views here.
def index(request): #То же самое, что News
    queryset = News.objects.all()
    return render(request, "Music_Up_Dev/index.html", {'content': queryset })

def Artists_view(request):
    return HttpResponse("Artists")

def Posts_view(request):
    return HttpResponse('Posts')

def Songs_view(request):
    return HttpResponse("Songs List")

def Load_a_Song(request):
    return HttpResponse('Load a Song')

def Create_a_Post(request):
    return HttpResponse('Create a Post')

def Create_a_News(request):
    return HttpResponse('Create a News')