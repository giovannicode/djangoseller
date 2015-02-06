from django.conf.urls import url, patterns

import views

urlpatterns = patterns('',
    url(r'^add', views.CartItemCreateView.as_view(), name='add')
)
