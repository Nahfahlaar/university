from rest_framework import viewsets
from .models import Student
from .serializers import *
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()



    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter('as_admin', openapi.IN_QUERY, description="Введите 1 если хотите увидеть все поля", type=openapi.TYPE_STRING)
    ])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def get_serializer_class(self):
        if self.request.method in ['GET']:
            if self.request.query_params.get('as_admin') == '1':
                return StudentAdminGetSerializer
            else:
                return StudentGetSerializer
        else:
            return StudentPostSerializer

