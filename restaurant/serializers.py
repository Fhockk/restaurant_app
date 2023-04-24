from rest_framework import serializers

from employees.models import Employee
from restaurant.models import Restaurant, Menu, Vote


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = (
            'id',
            'name'
        )


class MenuSerializer(serializers.ModelSerializer):
    count_of_votes = serializers.SerializerMethodField()

    class Meta:
        model = Menu
        fields = (
            'id',
            'restaurant',
            'date',
            'info',
            'count_of_votes'
        )

    def get_count_of_votes(self, obj):
        count = Vote.objects.filter(created_at=obj.date).filter(id=obj.id)
        return count


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = (
            'id',
            'employee',
            'menu',
            'created_at'
        )
        read_only_fields = ('created_at',)


