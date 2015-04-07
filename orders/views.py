from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Order


class OrderListView(ListView):
    model = Order

    def get_queryset(self):
        user = self.request.user
        return user.order_set.all().order_by('-date')

class OrderDetailView(DetailView):
    model = Order

    def get_queryset(self):
        queryset = super(OrderDetailView, self).get_queryset()
        return queryset.filter(user=self.request.user)
