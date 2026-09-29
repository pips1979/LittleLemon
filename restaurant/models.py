from django.db import models
from django.contrib.auth.models import User
from rest_framework import serializers


class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.SmallIntegerField()

    def __str__(self):
        return self.title
class MenuItem(models.Model):
	title = models.CharField(max_length=255)
	price = models.DecimalField(max_digits=6, decimal_places=2)
	inventory = models.SmallIntegerField()

	def get_item(self):
		return f'{self.title} : {str(self.price)}'

class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.SmallIntegerField()
    booking_date = models.DateTimeField()

    def __str__(self):
        return self.name