from django.conf.urls import url, patterns

import views

urlpatterns = patterns('',
    url(r'^create/(?P<product_id>[0-9]+)$', views.ReviewCreateView.as_view(), name='create'),
)
