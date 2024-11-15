from rest_framework import serializers
from .models import Student

class StudentGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['first_name', 'group']

class StudentPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"
class StudentAdminGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"
