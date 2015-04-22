from django.shortcuts import render
from rest_framework import generics, serializers

from orders.models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order


class OrderOffice(generics.ListAPIView): 
    model = Order
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
