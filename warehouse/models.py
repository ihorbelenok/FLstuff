from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Product(models.Model):
    class Meta(object):
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    name = models.CharField(max_length=254, blank=False, verbose_name="Product Name")
    unit = models.CharField(max_length=16, blank=False, verbose_name="Measurment unit")
    image = models.ImageField(upload_to='img/products/', blank=True, null=True, verbose_name="Product Image")
    inStock = models.DecimalField(max_digits=16, decimal_places=2, blank=False, verbose_name="Qty in stock")
    description = models.TextField(verbose_name="Description of product")

    def __unicode__(self):
        return u"%s" % self.name


class Company(models.Model):
    class Meta(object):
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

    name = models.CharField(max_length=254, blank=False, verbose_name="Contact Name")
    address = models.TextField(verbose_name="Address")
    phone = models.CharField(max_length=254, blank=False, verbose_name="Contact Phone")
    email = models.EmailField(max_length=254, blank=True, verbose_name="E-mail")
    comment = models.TextField(verbose_name="Comment")

    def __unicode__(self):
        return u"%s" % self.name


class Arrival(models.Model):
    class Meta(object):
        verbose_name = u'Product arrival'
        verbose_name_plural = u'Product arrivals'

    product = models.ForeignKey('Product', blank=False)
    supplier = models.ForeignKey('Company', blank=False)
    date = models.DateField(auto_now_add=True, verbose_name="Arrival Date")
    bestBefore = models.DateField(blank=True, null=True, verbose_name="Best Before")
    price = models.DecimalField(max_digits=16, decimal_places=2, blank=False, verbose_name="Price")
    quantity = models.DecimalField(max_digits=16, decimal_places=2, blank=False, verbose_name="Qty Arrived")
    inStock = models.DecimalField(max_digits=16, decimal_places=2, blank=False, verbose_name="Qty In Stock")

    def __unicode__(self):
        return u"%s from %s @ %s" % (self.product, self.supplier, self.arrivalDate)


class Dispatch(models.Model):
    class Meta(object):
        verbose_name = u'Dispatch'
        verbose_name_plural = u'Dispatches'

    product = models.ForeignKey('Product')
    distributor = models.ForeignKey('Company')
    date = models.DateField(auto_now_add=True, verbose_name="Dispatch Date")
    price = models.DecimalField(max_digits=16, decimal_places=2, blank=False, verbose_name="Price")
    quantity = models.DecimalField(max_digits=16, decimal_places=2, blank=False, verbose_name="Qty Dispatched")

    def __unicode__(self):
        return u"%s to %s @ %s" % (self.product, self.distributor, self.arrivalDate)


class Lot(models.Model):
    class Meta(object):
        verbose_name = u'Lot'
        verbose_name_plural = u'Lots'

    arrival = models.ForeignKey('Arrival')
    dispatch = models.ForeignKey('Dispatch')
    quantity = models.DecimalField(max_digits=16, decimal_places=2, blank=False, verbose_name="Qty Dispatched")

    def __unicode__(self):
        return u"%s to %s @ %s" % (self.arrival.product, self.dispatch.distributor, self.dispatch.date)
