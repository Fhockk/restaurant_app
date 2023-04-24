from rest_framework import generics, viewsets

from employees.models import Employee
from employees.serializers import EmployeeSerializer


class EmployeeModelViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
