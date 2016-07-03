from django.contrib import admin

from . import models

# Register your models here.
admin.site.register(models.Company)
admin.site.register(models.Client)
admin.site.register(models.Promotion)
admin.site.register(models.Coupon)
admin.site.register(models.Order)
admin.site.register(models.Position)
