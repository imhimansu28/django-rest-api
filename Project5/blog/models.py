from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to="media/")
    create = models.DateTimeField(auto_now=True)
    update = models.DateTimeField(auto_now_add=True,)
