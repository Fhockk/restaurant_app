import datetime

from django.db import models

from employees.models import Employee


class Restaurant(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True,
        blank=False
    )


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
