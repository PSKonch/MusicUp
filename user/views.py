from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import get_user, get_user_model

# Create your views here.


def login(request):
    return HttpResponse("Логин")

def logout(request):
    return HttpResponse("Логаут")

