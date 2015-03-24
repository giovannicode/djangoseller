from django.contrib import admin
from django.forms import SelectMultiple
from django.db import models

from .models import Product, Tag 
from categories.models import Category

class ProductAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ManyToManyField: {'widget': SelectMultiple(attrs={'size':'20'})}, 
    }

class TagAdmin(admin.ModelAdmin):
    ordering = ['category__name', 'name', 'value']

admin.site.register(Tag, TagAdmin)
admin.site.register(Product, ProductAdmin)
