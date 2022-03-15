from django.shortcuts import render
from .models import StudentDetails
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import io
from rest_framework.parsers import JSONParser



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


@csrf_exempt
def student_create(request):
 if request.method == 'POST':
  json_data = request.body
  stream = io.BytesIO(json_data)
  pythondata = JSONParser().parse(stream)
  serializer = StudentSerializer(data=pythondata)
  if serializer.is_valid():
   serializer.save()
   res = {'msg': 'Data Created'}
   json_data = JSONRenderer().render(res)
   return HttpResponse(json_data, content_type='application/json')
  json_data = JSONRenderer().render(serializer.errors)
  return HttpResponse(json_data, content_type='application/json')