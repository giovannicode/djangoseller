import json

from django.shortcuts import render, redirect
from django.views.generic import CreateView, TemplateView

from orders.models import Address

class CheckoutView(CreateView):
    model = Address
    template_name = 'checkout/index.html'

    def form_valid(self, form):
        address = form.save(commit=False)
        self.request.session['shipping_address'] = []
        json_address = self.request.session['shipping_address']
        json_address['street'] = address.street
        json_address['city'] = address.city
        json_address['state'] = address.state
        json_address['zip'] = address.zipcode  
        return redirect('main:index')
    
