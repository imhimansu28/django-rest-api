from pyexpat import model
from django.db import models

# Create your models here.

class StudentDetails(models.Model):
    stu_name = models.CharField(max_length=100)
    stu_class = models.IntegerField()
    stu_phone = models.CharField(max_length=20)
    stu_roll = models.CharField(max_length=10)
    city = models.CharField(max_length=100)

