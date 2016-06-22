from django.contrib import admin
from models import Product, Company, Arrival, Dispatch, Lot

# Register your models here.
admin.site.register(Product)
admin.site.register(Company)
admin.site.register(Arrival)
admin.site.register(Dispatch)
admin.site.register(Lot)
