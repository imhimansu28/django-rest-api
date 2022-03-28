from re import search
from turtle import update
from venv import create
from django.contrib import admin
from .models import Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ['title', 'create', 'update']
    filter = [create]

admin.site.register(Post,PostAdmin)


