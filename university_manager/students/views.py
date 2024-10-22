from rest_framework import viewsets
from .models import Student
from .serializers import *

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()

    def get_serializer_class(self):
        if self.request.method in ['GET']:
            if self.request.query_params.get('as_admin') == '1':
                return StudentAdminGetSerializer
            else:
                return StudentGetSerializer
        else:
            return StudentPostSerializer

