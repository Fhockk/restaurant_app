from datetime import date

from django.db import IntegrityError
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
        extra_kwargs = {
            "date": {"required": False},
        }

    def create(self, validated_data):
        restaurant = Restaurant.objects.get(id=self.context['request'].data.get('restaurant'))
        menu_date = self.context['request'].data.get('date') or date.today()
        info = self.context['request'].data.get('info')
        try:
            menu = Menu.objects.create(restaurant=restaurant, date=menu_date, info=info)
        except IntegrityError:
            raise serializers.ValidationError({
                'message': 'You have already added menu for that restaurant today.'
            })

        return menu

    def get_count_of_votes(self, obj):
        count = Vote.objects.filter(menu_id=obj.id, created_at=obj.date).count()
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
        extra_kwargs = {
            "employee": {"required": False},
        }

    def create(self, validated_data):
        employee = self.context['request'].user
        today = date.today()
        menu = Menu.objects.get(id=self.context['request'].data.get('menu'))
        if Vote.objects.filter(employee=employee, created_at=today, menu=menu).exists():
            raise serializers.ValidationError({
                'message': 'You have already voted today for this menu.'
            })
        vote = Vote.objects.create(employee=employee, created_at=today, menu=menu)
        return vote
