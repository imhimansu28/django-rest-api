from django import views
from django.urls import path

from blog import views

urlpatterns = [
    path('', views.index, name="home" ),
]
