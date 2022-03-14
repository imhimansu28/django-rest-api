from email.mime import base
from django.shortcuts import render
from .models import StudentDetails
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse



def home(request):
    return render(request, 'base.html')

# Model Object - Single Student Data
def student_detail(request, pk):
 stu = StudentDetails.objects.get(id = pk)
 # print(stu)
 serializer = StudentSerializer(stu)
 # print(serializer)
 # print(serializer.data)
 json_data = JSONRenderer().render(serializer.data)
 # print(json_data)
 return HttpResponse(json_data, content_type='application/json')
 # return JsonResponse(serializer.data)

# Create your views here.
def student_list(request):
 stu = StudentDetails.objects.all()
 # print(stu)
 serializer = StudentSerializer(stu, many=True)
 # print(serializer)
 # print(serializer.data)
#  json_data = JsonResponse(serializer.data)
 # print(json_data)
 return JsonResponse(serializer.data, safe=False)