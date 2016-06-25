from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=254)

    def __str__(self):
        return "%s" % self.name


class City(models.Model):
    name = models.CharField(max_length=254)
    country = models.ForeignKey("Country")

    def __str__(self):
        return "%s, %s" % (self.name, self.country)


class Hotel(models.Model):
    name = models.CharField(max_length=254)

    # stars rating
    rating = models.IntegerField()

    # for google maps API
    latitude = models.FloatField()
    longitude = models.FloatField()

    city = models.ForeignKey("City")

    email = models.EmailField()
    phone = models.CharField(max_length=16)
    fax = models.CharField(max_length=16)
    homepage = models.URLField()

    description = models.TextField()


class Tour(models.Model):
    hotel = models.ForeignKey("Hotel")
    start_date = models.DateField()
    end_date = models.DateField()
    price = models.DecimalField(decimal_places=2, max_digits=8)
    total_places = models.IntegerField()
    available_places = models.IntegerField()
    description = models.TextField()


class Client(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    birthdate = models.DateField()

    # new offers subscription
    subscription = models.BooleanField(default=True)


class Phone(models.Model):
    address = models.CharField(max_length=16)
    client = models.ForeignKey("Client")


class Email(models.Model):
    address = models.EmailField()
    client = models.ForeignKey("Client")


class OrderStatus(models.Model):
    name = models.CharField(max_length=254)

    def __str__(self):
        return "%s" % self.name


class Order(models.Model):
    client = models.ForeignKey("Client")
    tour = models.ForeignKey("Tour")
    places = models.IntegerField()
    discount = models.DecimalField(decimal_places=2, max_digits=8)
    total = models.DecimalField(decimal_places=2, max_digits=8)
    status = models.ForeignKey("OrderStatus")