from datetime import date

from rest_framework import generics
from django.db.models import Count

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


class CurrentDayMenuListAPIView(generics.ListAPIView):
    queryset = Menu.objects.filter(date=date.today())
    serializer_class = MenuSerializer


class VoteCreateAPIView(generics.CreateAPIView):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer


class CurrentDayResultsListAPIView(generics.ListAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    def get_queryset(self):
        today = date.today()
        queryset = Menu.objects.filter(date=today).annotate(count_of_votes=Count('votes')).order_by('-count_of_votes')
        return queryset


