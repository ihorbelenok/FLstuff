from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=64)
    address = models.CharField(max_length=128)
    phone = models.CharField(max_length=16)
    fax = models.CharField(max_length=16)
    email = models.EmailField()
    description = models.TextField()

    def __str__(self):
        return "%s" % self.name


class Client(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    phone = models.CharField(max_length=16)
    email = models.EmailField()

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


class Promotion(models.Model):
    company = models.ForeignKey("Company")
    name = models.CharField(max_length=64)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return "%s by %s (%s - %s)" % (self.name, self.company, self.start_date, self.end_date)


class Coupon(models.Model):
    promotion = models.ForeignKey("Promotion")
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    discount = models.DecimalField(max_digits=4, decimal_places=2)
    quantity = models.IntegerField()

    def __str__(self):
        return "%s%% for %s" % (self.first_name, self.promotion.name)


class Order(models.Model):
    client = models.ForeignKey("Client")
    total = models.DecimalField(max_digits=8, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s @ %s" % (self.client, self.date)


class Position(models.Model):
    order = models.ForeignKey("Order")
    coupon = models.ForeignKey("Coupon")
    quantity = models.IntegerField()

    def __str__(self):
        return "%d of %s (order: %s)" % (self.quantity, self.coupon, self.order)
