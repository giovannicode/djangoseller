from django.conf.urls import url, patterns
from rest_framework.urlpatterns import format_suffix_patterns

import views

urlpatterns = patterns('',
    url(r'^$', views.DashboardView.as_view(), name='index'),
    url(r'^login', views.AdminLoginView.as_view(), name='login'),
    url(r'^orders/list', views.OrderListView.as_view(), name='order_list')
)

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json'])
