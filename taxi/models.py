from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Client(models.Model):
    phone = models.CharField(max_length=32)
    name = models.CharField(max_length=32)
    lastOrder = models.DateField()
    orders = models.PositiveIntegerField()

    def __str__(self):
        return "%s (%s)" % (self.phone, self.name)


class Auto(models.Model):
    number = models.CharField(max_length=32)
    brand = models.CharField(max_length=32)
    color = models.CharField(max_length=32)

    def __str__(self):
        return "%s %s" % (self.brand, self.number)


class Driver(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    license = models.CharField(max_length=32)
    auto = models.ForeignKey("Auto")
    available = models.BooleanField(default=True)

    def __str__(self):
        return "%s %s" % (self.last_name, self.first_name)


class Order(models.Model):
    client = models.ForeignKey("Client")
    source = models.CharField(max_length=254)
    destination = models.CharField(max_length=254)
    driver = models.ForeignKey("Driver")
    received = models.DateTimeField(auto_created=True)
    picked = models.DateTimeField(blank=True, null=True, default=None)
    delivered = models.DateTimeField(blank=True, null=True, default=None)
    distance = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    discount = models.BooleanField(default=False)

    def __str__(self):
        return "%s --> %s" % (self.source, self.destination)
