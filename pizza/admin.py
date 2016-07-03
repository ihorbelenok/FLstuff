from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Discount)
admin.site.register(models.OrderStatus)
admin.site.register(models.ProductType)

admin.site.register(models.Client)
admin.site.register(models.ClientPhone)

admin.site.register(models.Courier)
admin.site.register(models.CourierPhone)

admin.site.register(models.Product)
admin.site.register(models.Position)
admin.site.register(models.Order)
