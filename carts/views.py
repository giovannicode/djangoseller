from django.db import IntegrityError, transaction
from django.db.models import F
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, DeleteView
from django.http import HttpResponse

from rest_framework import generics
from rest_framework.response import Response

from main.functions import *

from .models import Cart, CartItem
from products.models import Product

from .serializers import CartItemSerializer

class CartCreateRest(TemplateView):
    template_name = 'notemplate'

    def get(self, request, *args, **kwargs):
        product = Product.objects.get(pk=request.GET.get('product_id'))
        cart = get_cart(self)

        # Check to make sure the item is not already in the cart. 
        if not cart.cartitem_set.filter(product=product).exists():
            try:
                with transaction.atomic():
                    cart.cartitem_set.create(cart=cart, product=product, qty=1)
                    Product.objects.filter(id=product.id).update(qty=F('qty')-1)
            except IntegrityError:
                raise IntegrityError 
        # If the item is already in the cart, update the quantity instead. 
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
                cart = get_cart(self) 
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
        cart = get_cart(self)
        return cart

class CartItemListAPI(generics.ListAPIView):  
    serializer_class = CartItemSerializer

    def get_queryset(self):
        cart = get_cart(self) 
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
        cart = get_cart(self) 
        self.queryset = cart.cartitem_set.all()
        return super(CartItemUpdateAPI, self).get_queryset()

    def post(self, request, *args, **kwargs):
        return self.patch(request, *args, **kwargs)
