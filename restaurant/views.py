from datetime import date

from rest_framework import generics

from employees.models import Employee
from restaurant.models import Restaurant, Menu, Vote
from restaurant.serializers import (
    RestaurantSerializer, MenuSerializer, VoteSerializer
)


class RestaurantCreateAPIView(generics.CreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class MenuCreateAPIView(generics.CreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer



