from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Student
from .serializers import *
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                "as_role",
                openapi.IN_QUERY,
                description="Введите 'admin' для получения всей информации или 'user' для пользовательской информации",
                type=openapi.TYPE_STRING,
                enum=["admin", "user"],
            )
        ],
        responses={
            "200": openapi.Response(
                description="Ответ при зачении 'admin'",
                schema=StudentAdminGetSerializer,
            ),
            "200 ": openapi.Response(
                description="Ответ при значении 'user'", schema=StudentGetSerializer
            ),
            "400 ": openapi.Response(description="Некоректный параметр 'as_role'"),
        },
    )
    def list(self, request, *args, **kwargs):
        as_role = request.query_params.get("as_role")
        if as_role not in ["admin", "user"]:
            return Response(
                {"detail": "Параметр 'as_role' должен быть 'admin' или 'user'."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return super().list(request, *args, **kwargs)

    def get_serializer_class(self):
        if getattr(self, "swagger_fake_view", False):
            return StudentGetSerializer

        if self.request.method in ["GET"]:
            if self.request.query_params.get("as_role") == "admin":
                return StudentAdminGetSerializer
            elif self.request.query_params.get("as_role") == "user":
                return StudentGetSerializer
        else:
            return StudentPostSerializer
