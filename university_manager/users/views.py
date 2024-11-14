from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserRegistrationSerializer
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

from students.serializers import StudentPostSerializer

@api_view(['POST'])
def register_user(request):
    if request.method == 'POST':
        serializer = UserRegistrationSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response({"detail": "Username и пароль обязательны."}, status=status.HTTP_400_BAD_REQUEST)


    user = authenticate(request, username=username, password=password)

    if user is None:
        return Response({"detail": "Неверный username или пароль."}, status=status.HTTP_401_UNAUTHORIZED)

    token, created = Token.objects.get_or_create(user=user)

    student = user.student_profile
    student_serializer = StudentPostSerializer(student)

    return Response({
        'student_profile': student_serializer.data,
    })