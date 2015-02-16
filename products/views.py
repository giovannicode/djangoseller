from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Product
from categories.models import Category

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from django.core import serializers
from django.http import JsonResponse

from .serializers import ProductSerializer
from rest_framework import generics

class ProductListView(ListView):
    model = Product
    
    @method_decorator(csrf_exempt) 
    def dispatch(self, *args, **kwargs):
        return super(ProductListView, self).dispatch(*args, **kwargs)
 
    def post(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        stuff = queryset.filter(categories__id=request.POST['category_id'])
        data = serializers.serialize('json', stuff) 
        return JsonResponse(data, safe=False) 
   
    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        return context

    def get_queryset(self): 
        queryset = super(ProductListView, self).get_queryset()
        q = self.request.GET.get("q")
        if not q:
            return queryset
        elif q == "asc":
            return queryset.all().order_by('price')
        elif q == "dsc":
            return queryset.all().order_by('-price')
        return queryset

class ProductDetailView(DetailView):
    model = Product


class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_fields = ('name', 'price')
    #renderer_classes = [JSONRenderer]

