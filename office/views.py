from django.shortcuts import render
from rest_framework import generics, serializers

from orders.models import Order

class OrderSerializer(serializers.OrderSerializer):
    class Meta:
        model = Order


class OrderOffice(RetriveAPIView): 
    model = Order
    serializer_class = OrderSerializer
