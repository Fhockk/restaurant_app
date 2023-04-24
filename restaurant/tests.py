from datetime import date, timedelta

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from employees.models import Employee
from restaurant.models import Restaurant, Menu, Vote


class TestRestaurantCreateAPIView(APITestCase):
    def setUp(self):
        self.admin_user = Employee.objects.create_superuser(
            username='admin', email='admin@example.com', password='password'
        )
        self.client.force_authenticate(user=self.admin_user)
        self.restaurant_data = {'name': 'Test Restaurant'}

    def test_create_restaurant(self):
        url = reverse('create_restaurant')
        response = self.client.post(url, self.restaurant_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Restaurant.objects.count(), 1)
        self.assertEqual(Restaurant.objects.get().name, 'Test Restaurant')


class TestMenuCreateAPIView(APITestCase):
    url = reverse('create_menu')

    def setUp(self):
        self.admin_user = Employee.objects.create_superuser(
            username='admin', email='admin@example.com', password='password'
        )
        self.client.force_authenticate(user=self.admin_user)
        self.restaurant = Restaurant.objects.create(name='Test Restaurant')

    def test_create_menu(self):
        menu_data = {
            'restaurant': self.restaurant.id,
            'date': date.today(),
            'info': 'Test Menu'
        }
        response = self.client.post(self.url, menu_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Menu.objects.count(), 1)
        menu = Menu.objects.first()
        self.assertEqual(menu.restaurant, self.restaurant)
        self.assertEqual(menu.date, date.today())
        self.assertEqual(menu.info, 'Test Menu')


class TestCurrentDayMenuListAPIView(APITestCase):
    def setUp(self):
        self.restaurant = Restaurant.objects.create(name='Test Restaurant')
        self.today_menu = Menu.objects.create(
            restaurant=self.restaurant,
            date=date.today(), info='Today Menu'
        )
        self.yesterday_menu = Menu.objects.create(
            restaurant=self.restaurant,
            date=date.today()-timedelta(days=1),
            info='Yesterday Menu'
        )
        self.user = Employee.objects.create_user(
            username='John', email='john@example.com', password='password'
        )
        self.client.force_authenticate(user=self.user)

    def test_get_current_day_menu(self):
        url = reverse('current_day_menu')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        menu = response.data[0]
        self.assertEqual(menu['id'], self.today_menu.id)
        self.assertEqual(menu['restaurant'], self.restaurant.id)
        self.assertEqual(menu['date'], str(date.today()))
        self.assertEqual(menu['info'], 'Today Menu')
        self.assertEqual(menu['count_of_votes'], 0)


class TestVoteCreateAPIView(APITestCase):
    def setUp(self):
        self.restaurant = Restaurant.objects.create(name='Test Restaurant')
        self.menu = Menu.objects.create(
            restaurant=self.restaurant, date=date.today(), info='Today Menu'
        )
        self.user = Employee.objects.create_user(
            username='user', email='user@example.com', password='password'
        )
        self.client.force_authenticate(user=self.user)

    def test_create_vote(self):
        url = reverse('create_vote')
        data = {
            'menu': self.menu.id,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Vote.objects.count(), 1)
        vote = Vote.objects.first()
        self.assertEqual(vote.employee, self.user)
        self.assertEqual(vote.menu, self.menu)
        self.assertEqual(vote.created_at, date.today())

    def test_create_vote_already_voted(self):
        Vote.objects.create(employee=self.user, menu=self.menu, created_at=date.today())
        url = reverse('create_vote')
        data = {
            'menu': self.menu.id,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['message'], 'You have already voted today for this menu.')
        self.assertEqual(Vote.objects.count(), 1)
