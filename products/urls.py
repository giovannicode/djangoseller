from django.conf.urls import url, patterns
from rest_framework.urlpatterns import format_suffix_patterns

import views

urlpatterns = patterns('',
    url(r'^list', views.ProductListView.as_view(), name='list'),
    url(r'^detail/(?P<pk>[0-9]+)$', views.ProductDetailView.as_view(), name='detail'),
    url(r'^api/list', views.ProductListAPI.as_view(), name='api_list')
) 

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json'])
