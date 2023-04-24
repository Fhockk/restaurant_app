from django.urls import path

from restaurant.views import (
    RestaurantCreateAPIView, MenuCreateAPIView, CurrentDayMenuListAPIView,
    VoteCreateAPIView, CurrentDayResultsListAPIView
)


urlpatterns = [
    path('restaurant/', RestaurantCreateAPIView.as_view(), name='create_restaurant'),
    path('menu/', MenuCreateAPIView.as_view(), name='create_menu'),
    path('menu/today/', CurrentDayMenuListAPIView.as_view(), name='current_day_menu'),
    path('vote/', VoteCreateAPIView.as_view(), name='create_vote'),
    path('vote/today/', CurrentDayResultsListAPIView.as_view(), name='current_day_results')
]
