from django.contrib import admin
from . import models

# Register your models here.

admin.register(models.Country)
admin.register(models.City)
admin.register(models.Hotel)
admin.register(models.Tour)
admin.register(models.Client)
admin.register(models.Email)
admin.register(models.Phone)
admin.register(models.OrderStatus)
admin.register(models.Order)