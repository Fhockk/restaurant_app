from django.urls import path, include
from rest_framework import routers
from employees.views import EmployeeModelViewSet

router = routers.SimpleRouter()
router.register(r'employees', EmployeeModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
