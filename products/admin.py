from django.contrib import admin

from .models import Product, Filter 

admin.site.register(Filter)
admin.site.register(Product)
