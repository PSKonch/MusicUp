from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Ok")

def News(request):
    return HttpResponse("news")

def Artists(request):
    return HttpResponse("Artists")

