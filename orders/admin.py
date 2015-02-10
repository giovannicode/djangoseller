from django.contrib import admin

from .models import Address, Order, OrderItem
from payments.models import Payment


class OrderItemInline(admin.StackedInline):
    model = OrderItem
    readonly_fields=['product', 'title', 'price', 'qty']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    readonly_fields=['user', 'email', 'payment', 'address']
    inlines=[OrderItemInline] 
