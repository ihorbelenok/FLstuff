from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Discount(models.Model):
    min_value = models.PositiveIntegerField()
    max_value = models.PositiveIntegerField()
    percent = models.PositiveIntegerField()

    def __str__(self):
        return "%d%% (%d - %d)" % (self.percent, self.min_value, self.max_value)


class ProductType(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return "%s" % self.name


class Product(models.Model):
    name = models.CharField(max_length=128)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    product_type = models.ForeignKey("ProductType")
    description = models.TextField(blank=True)

    def __str__(self):
        return "%s" % self.name


class Client(models.Model):
    name = models.CharField(max_length=64)
    address = models.CharField(max_length=64)

    def __str__(self):
        return "%s @ %s" % (self.name, self.address)


class ClientPhone(models.Model):
    number = models.CharField(max_length=16)
    client = models.ForeignKey("Client")

    def __str__(self):
        return "%s's phone" % self.client


class Courier(models.Model):
    name = models.CharField(max_length=64)
    available = models.BooleanField()

    def __str__(self):
        return "%s" % self.name


class CourierPhone(models.Model):
    number = models.CharField(max_length=16)
    courier = models.ForeignKey("Courier")

    def __str__(self):
        return "%s's phone" % self.courier


class OrderStatus(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return "%s" % self.name


class Order(models.Model):
    client = models.ForeignKey("Client")
    courier = models.ForeignKey("Courier")
    time = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    discount = models.ForeignKey("Discount")
    status = models.ForeignKey("OrderStatus")

    def __str__(self):
        return "%s %s" % (self.time, self.client)


class Position(models.Model):
    order = models.ForeignKey("Order")
    product = models.ForeignKey("Product")
    quantity = models.IntegerField()

    def __str__(self):
        return "%s (%s)" % (self.product, self.order)
