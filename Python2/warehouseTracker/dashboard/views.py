from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
from django.contrib.auth.models import User, auth
from django.contrib import messages


# Create your views here.

def Packages(request):
    tracklist = Item.object.all()
    return render(request, 'templates/trackpage.html')

def index(request):
    return render(request, 'mainpage.html')

def track(request):
    return render(request, 'trackpage.html')

def display(request, pk):
    package = Item.object.get(id=pk)
    return render(request,'templates/trackpage.html'),