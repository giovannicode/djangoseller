from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('main.urls', namespace='main')),
    url(r'^products/', include('products.urls', namespace='products')),
    url(r'^carts/', include('carts.urls', namespace='carts')),
    url(r'^checkout/', include('checkout.urls', namespace='checkout'))
)
