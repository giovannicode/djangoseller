from django.shortcuts import render
from django.views.generic import ListView 
from django.contrib.admin import forms
from rest_framework import generics, serializers

from orders.models import Order

class AdminLoginView(AnonymousRequiredMixin, FormView):
    authenticated_redirect_url = u"/"
    template_name = 'office/login.html'
    form_class = AdminAuthenticationForm

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order

class OrderListView(ListView):
    model = Order
    template_name = 'office/object_list.html'


class OrderOffice(generics.ListAPIView): 
    model = Order
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
