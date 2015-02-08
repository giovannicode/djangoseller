from django.conf.urls import url, patterns

import views

urlpatterns = patterns('',
    url(r'^$', views.CheckoutView.as_view(), name='index')
)
