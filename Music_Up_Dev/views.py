from django.shortcuts import render
from django.http import HttpResponse
from .models import CustomUser

# Create your views here.
def index(request):
    queryset = CustomUser.objects.all()
    return render(request, "Music_Up_Dev/index.html", {'content': queryset })

def News(request):
    return HttpResponse("news")

def Artists(request):
    return HttpResponse("Artists")

def Posts(request):
    return HttpResponse('posts')