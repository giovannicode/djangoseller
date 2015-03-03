from django.core.execption import DoesNotExist
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
        if request.user.is_authenticated():
            return self.foo(request)
        else:
            return self.foo2(request)

    def foo(self, request): 
        cart = request.user.cart
        if not cart.cartitem_set.filter(product=product).exists():
            try:
                with transaction.atomic():
                    cart.cartitem_set.create(cart=cart, product=product, qty=1)
                    Product.objects.filter(id=product.id).update(qty=F('qty')-1)
            except IntegrityError:
                raise IntegrityError 
        else:
            try:
                with transaction.atomic():
                    cart.cartitem_set.filter(product=product).update(qty=F('qty')+1) 
                    Product.objects.filter(id=product.id).update(qty=F('qty')-1)
            except IntegrityError:
                raise IntegrityError
        return HttpResponse('Item added')

    def foo2(self, request):
        # May update and  try-catch later, as I will it is ugly implementation
        try: 
            Cart.objects.get(session_key=request.session.session_key)
            return HttpResponse('Old Card has been found')
        except DoesNotExist:
            cart = Cart.objects.create(session_key=request.session.session_key)
            return HttpResponse('New Cart Created')

class CartDetailView(DetailView):
    model = Cart

    def get_object(self): 
        return Cart.objects.get(pk=self.request.user.cart.id)
