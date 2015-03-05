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
            return self.auth_cart_add(request, product)
        else:
            return self.anom_cart_add(request, product)

    def auth_cart_add(self, request, product): 
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

    def anom_cart_add(self, request, product):
        # May update try-catch later, as I think it is an ugly implementation
        try: 
            # Setting modified to True will make sure that session_key is not None
            request.session.modified = True
            cart = Cart.objects.get(session_key=request.session.session_key)
        except Cart.DoesNotExist:
            cart = Cart.objects.create(session_key=request.session.session_key)

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


class CartItemDeleteView(DeleteView):
    model = CartItem

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        succes_url


class CartDetailView(DetailView):
    model = Cart

    def get_object(self): 
        if self.request.user.is_authenticated():
            return Cart.objects.get(pk=self.request.user.cart.id)
        else: 
            # May update try-catch later, as I think it is an ugly implementation
            try: 
                # Setting modified to True will make sure that session_key is not None
		self.request.session.modified = True
		cart = Cart.objects.get(session_key=self.request.session.session_key)
	    except Cart.DoesNotExist:
		cart = Cart.objects.create(session_key=self.request.session.session_key)
            return cart
