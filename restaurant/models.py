from django.db import models

from employees.models import Employee


class Restaurant(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True,
        blank=False
    )

    def __str__(self):
        return f'Restaurant {self.pk}, name is {self.name}'


class Menu(models.Model):
    restaurant = models.ForeignKey(
        to=Restaurant,
        on_delete=models.CASCADE,
        related_name='menu'
    )
    date = models.DateField()
    info = models.TextField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['restaurant', 'date'], name='unique_menu')
        ]

    def __str__(self):
        return f'Menu: Restaurant {self.restaurant.name}, date: {self.date}'


class Vote(models.Model):
    employee = models.ForeignKey(
        to=Employee,
        on_delete=models.CASCADE,
        related_name='vote'
    )
    menu = models.ForeignKey(
        to=Menu,
        on_delete=models.CASCADE,
        related_name='votes'
    )
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return f'Vote: Employee {self.employee.get_full_name()}, menu: {self.menu.info}'
