from django.contrib import admin
from django.forms import SelectMultiple
from django.db import models

from .models import Product, Tag 

class ProductAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ManyToManyField: {'widget': SelectMultiple(attrs={'size':'20'})}, 
    }

admin.site.register(Tag)
admin.site.register(Product, ProductAdmin)
