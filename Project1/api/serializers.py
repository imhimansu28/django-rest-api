from unicodedata import name
from rest_framework import serializers
class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    stu_name = serializers.CharField(max_length=100)
    stu_class = serializers.IntegerField()
    stu_phone = serializers.CharField(max_length=20)
    stu_roll = serializers.CharField(max_length=10)
    city = serializers.CharField(max_length=100)