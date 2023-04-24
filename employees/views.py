from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from employees.models import Employee
from employees.serializers import EmployeeSerializer


class EmployeeModelViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [AllowAny]
