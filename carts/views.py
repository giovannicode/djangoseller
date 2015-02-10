from django.db.models import F
from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from django.http import HttpResponse

from .models import Cart
from products.models import Product

class CartCreateRest(TemplateView):
    template_name = 'notemplate'

    def post(self, request, *args, **kwargs):
        product = Product.objects.get(pk=request.POST.get('product_id'))
        cart = request.user.cart
        if not cart.cartitem_set.filter(product=product).exists():
            cart.cartitem_set.create(cart=cart, product=product, qty=1)
        else:
            cart.cartitem_set.filter(product=product).update(qty=F('qty')+1) 
        return HttpResponse('Item added')
        

class CartDetailView(DetailView):
    model = Cart

