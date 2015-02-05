from django.conf.urls import url, patterns

import views

urlpatterns = patterns('',
    url(r'^list', views.ProductListView.as_view(), name='list')
) 
