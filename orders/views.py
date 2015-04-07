from django.shortcuts import render
from django.views.generic.list import ListView

from .models import Order


class OrderListView(ListView):
    model = Order

    def get_queryset(self):
        user = self.request.user
        return user.order_set.all()

