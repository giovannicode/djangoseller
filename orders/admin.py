from django.contrib import admin

from .models import Address, Order, OrderItem
from payments.models import Payment


class OrderItemInline(admin.StackedInline):
    model = OrderItem
    readonly_fields=['product', 'title', 'price', 'qty']
    extra=0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    readonly_fields=['user', 'email', 'date', 'payment', 'address']
    inlines=[OrderItemInline] 
