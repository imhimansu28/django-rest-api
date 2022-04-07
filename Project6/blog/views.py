from django import views
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse("Hi I am Django Python Web FrameWork")

