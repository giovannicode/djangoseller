from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.views.generic import ListView, FormView, TemplateView
from django.contrib.admin.forms import AdminAuthenticationForm

from braces.views import AnonymousRequiredMixin, StaffuserRequiredMixin

from rest_framework import generics, serializers

from orders.models import Order

class AdminLoginView(AnonymousRequiredMixin, FormView):
    authenticated_redirect_url = u"/"
    template_name = 'office/login.html'
    form_class = AdminAuthenticationForm

    def form_valid(self, form):
        login(self.request, form.get_user())
        return redirect('office:index')

class DashboardView(StaffuserRequiredMixin, TemplateView):
    template_name = u"office/index.html"


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
