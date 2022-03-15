from django.contrib import admin
from .models import StudentDetails
# Register your models here.
@admin.register(StudentDetails)
class StudentDetailsAdmin(admin.ModelAdmin):
    list_display = ['id', 'stu_name', 'stu_class', 'stu_phone', 'stu_roll', 'city' ]