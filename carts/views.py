from django.db import IntegrityError, transaction
from django.db.models import F
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, DeleteView
from django.http import HttpResponse

from rest_framework import generics
from rest_framework.response import Response

from .models import Cart, CartItem
from products.models import Product

from .serializers import CartItemSerializer

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
    success_url = '/carts/detail'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        try:
            with transaction.atomic():
                if self.request.user.is_authenticated(): 
                    cart = self.request.user.cart
                else:
                    cart = Cart.objects.get(session_key=self.request.session.session_key)
                cart_item = cart.cartitem_set.get(id=self.object.id)
                Product.objects.filter(id=cart_item.product.id).update(qty=F('qty')+cart_item.qty)
                cart_item.delete()
        except:
            raise
        return HttpResponse('item removed from cart')
  
    # Add get method to make it easier to work with angular
    def get(self,request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


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


class CartItemListAPI(generics.ListAPIView):  
    serializer_class = CartItemSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated():
            cart = self.request.user.cart
        else:
           cart = Cart.objects.get(session_key=self.request.session.session_key) 
        self.queryset = cart.cartitem_set.all()
        return super(CartItemListAPI, self).get_queryset()


class CartItemUpdateAPI(generics.UpdateAPIView):
    serializer_class = CartItemSerializer

    def update(self, request, *args, **kwargs): 
        partial = kwargs.pop('partial', False)
        instance = self.get_object()

        old_qty = instance.qty
        new_qty = request.data['qty'] 
        diff_qty = old_qty - int(new_qty) 
        
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
 
        try:
            with transaction.atomic():
                product = Product.objects.get(id=instance.product.id)
                if product.qty < -diff_qty:
                    return HttpResponseBadRequest("I'm sorry we only have (" + str(product.qty) + ") of that item left")
                Product.objects.filter(id=instance.product.id).update(qty=F('qty')+diff_qty)
                self.perform_update(serializer) 
        except:
            raise
        return Response(diff_qty)

    def get_queryset(self):
        if self.request.user.is_authenticated():
            cart = self.request.user.cart
        else:
           cart = Cart.objects.get(session_key=self.request.session.session_key) 
        self.queryset = cart.cartitem_set.all()
        return super(CartItemUpdateAPI, self).get_queryset()

    def post(self, request, *args, **kwargs):
        return self.patch(request, *args, **kwargs)
