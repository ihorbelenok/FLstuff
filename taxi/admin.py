from django.contrib import admin
from . import models

# Register your models here.
admin.register(models.Auto)
admin.register(models.Driver)
admin.register(models.Client)
admin.register(models.Order)
