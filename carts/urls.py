from django.conf.urls import url, patterns
from rest_framework.urlpatterns import format_suffix_patterns

import views

urlpatterns = patterns('',
    url(r'^add', views.CartCreateRest.as_view(), name='add'),
    url(r'^detail', views.CartDetailView.as_view(), name='detail'),
    url(r'^delete/(?P<pk>\d+)/$', views.CartItemDeleteView.as_view(), name='delete'),
    url(r'^api/list', views.CartItemListAPI.as_view(), name='api_list'),
    url(r'^api/update/(?P<pk>\d+)/$', views.CartItemUpdateAPI.as_view(), name='api_list') 
)

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json'])
