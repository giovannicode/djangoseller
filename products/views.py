from django.views.generic import DetailView, ListView
from rest_framework import generics, filters

import django_filters

from .models import Product
from .forms import FilterForm, ShirtFilterForm
from .serializers import ProductSerializer
from categories.models import Category

class ProductListView(ListView):
    model = Product
    filter_form_class = ShirtFilterForm
       
    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.exclude(name='All')
        context['filter_form'] = self.filter_form_class() 
        return context


class ProductDetailView(DetailView):
    model = Product
    

# API Views.
class ProductListAPI(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    filter_fields = ('name', 'price', 'categories', 'color', 'tags')
    filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter,)
    ordering_fields = ('price', 'color')

    def get_queryset(self):
        queryset = Product.objects.all()
        tags = self.request.QUERY_PARAMS.getlist('tags')
        #queryset = queryset.filter(tags__in=tags)

        for tag in tags:
            queryset = queryset.filter(tags=tag)
        return queryset
        
    #renderer_classes = [JSONRenderer]
