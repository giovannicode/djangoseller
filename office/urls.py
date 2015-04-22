from django.conf.urls import url, patterns
from rest_framework.urlpatterns import format_suffix_patterns

import views

urlpatterns = patterns('',
    url(r'^list', views.OrderOffice.as_view(), name='order_list')
)

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json'])
