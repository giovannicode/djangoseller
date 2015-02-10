from django.conf.urls import url, patterns

import views

urlpatterns = patterns('',
    url(r'^list', views.ProductListView.as_view(), name='list'),
    url(r'^detail/(?P<pk>[0-9]+)$', views.ProductDetailView.as_view(), name='detail')
) 
