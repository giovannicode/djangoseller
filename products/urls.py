from django.conf.urls import url, patterns
from rest_framework.urlpatterns import format_suffix_patterns

import views

from .forms import *

urlpatterns = patterns('',
    url(r'^1/list', views.ProductListView.as_view(filter_form_class=ShirtFilterForm), name='shirts-list'),
    url(r'^2/list', views.ProductListView.as_view(filter_form_class=PantsFilterForm)),
    url(r'^4/list', views.ProductListView.as_view(filter_form_class=ShortsFilterForm)),
    url(r'^5/list', views.ProductListView.as_view(filter_form_class=LongSleeveFilterForm)),
    url(r'^6/list', views.ProductListView.as_view(filter_form_class=HatsFilterForm)),
    url(r'^7/list', views.ProductListView.as_view(filter_form_class=ShoesFilterForm)),
    url(r'^list', views.ProductListView.as_view(), name='list'),
    url(r'^detail/(?P<pk>[0-9]+)$', views.ProductDetailView.as_view(), name='detail'),
    url(r'^api/list', views.ProductListAPI.as_view(), name='api_list')
) 

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json'])
