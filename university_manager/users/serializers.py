from rest_framework import serializers
from students.models import Student
from django.contrib.auth import get_user_model
from students.serializers import StudentPostSerializer

User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    student_profile = StudentPostSerializer()
    username = serializers.CharField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'phone_number', 'student_profile']

    def create(self, validated_data):
        student_data = validated_data.pop('student_profile')
        user = User.objects.create_user(**validated_data)
        Student.objects.create(user=user, **student_data)
        return user