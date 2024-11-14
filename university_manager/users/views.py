from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserRegistrationSerializer
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from students.serializers import StudentPostSerializer


# @swagger_auto_schema(
#     method="post",
#     request_body=UserRegistrationSerializer,
#     responses={
#         201: openapi.Response('Пользователь зарегестрирован успешно', UserRegistrationSerializer),
#         400: "Invalid data",
#     },
#
# )


@swagger_auto_schema(
    method="post",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'username': openapi.Schema(type=openapi.TYPE_STRING),
            'email': openapi.Schema(type=openapi.TYPE_STRING),
            'password': openapi.Schema(type=openapi.TYPE_STRING),
            'phone_number': openapi.Schema(type=openapi.TYPE_STRING),
            'student_profile': openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'first_name': openapi.Schema(type=openapi.TYPE_STRING),
                    'last_name': openapi.Schema(type=openapi.TYPE_STRING),
                    'group': openapi.Schema(type=openapi.TYPE_STRING),
                    'specialization': openapi.Schema(type=openapi.TYPE_STRING),
                },
                required=['first_name', 'last_name', 'group', 'specialization']
            ),
        },
        required=['username', 'email', 'password', 'phone_number', 'student_profile'],
    ),
    responses={
        201: openapi.Response('Пользователь зарегистрирован успешно', UserRegistrationSerializer),
        400: "Invalid data",
    },
)
@api_view(['POST'])
def register_user(request):
    if request.method == 'POST':
        serializer = UserRegistrationSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    method='post',
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'username': openapi.Schema(type=openapi.TYPE_STRING, description='Имя пользователя'),
            'password': openapi.Schema(type=openapi.TYPE_STRING, description='Пароль'),
        },
        required=['username', 'password'],
    ),
    responses={
        200: openapi.Response(
            'Успешный вход',
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'student_profile': openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        description='Данные профиля студента',
                        additional_properties=openapi.Schema(type=openapi.TYPE_STRING)
                    ),
                },
            )
        ),
        400: "Username и пароль обязательны.",
        401: "Неверный username или пароль.",
    }
)
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