from django.db import IntegrityError, transaction
from django.db.models import F
from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from django.http import HttpResponse

from .models import Cart
from products.models import Product

class CartCreateRest(TemplateView):
    template_name = 'notemplate'

    def get(self, request, *args, **kwargs):
        product = Product.objects.get(pk=request.GET.get('product_id'))
        cart = request.user.cart
        if not cart.cartitem_set.filter(product=product).exists():
            try:
                with transaction.atomic():
                    cart.cartitem_set.create(cart=cart, product=product, qty=1)
                    Products.objects.filter(product=product).update(qty=F('qty')-1)
            except IntegrityError:
                raise IntegrityError 
        else:
            try:
                with transaction.atomic():
                    cart.cartitem_set.filter(product=product).update(qty=F('qty')+1) 
                    Products.objects.filter(product=product).update(qty=F('qty')-1)
            except IntegrityError:
                raise IntegrityError
        return HttpResponse('Item added')
        

class CartDetailView(DetailView):
    model = Cart

    def get_object(self): 
        return Cart.objects.get(pk=self.request.user.cart.id)

