from django.views.generic import DetailView, ListView
from rest_framework import generics, filters

from .models import Product
from .forms import FilterForm
from .serializers import ProductSerializer
from categories.models import Category

class ProductListView(ListView):
    model = Product
       
    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        context['filter_form'] = FilterForm()
        return context


class ProductDetailView(DetailView):
    model = Product


# API Views.
class ProductListAPI(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_fields = ('name', 'price', 'categories', 'color', 'filter')
    filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter,)
    ordering_fields = ('price', 'color')
    #renderer_classes = [JSONRenderer]

