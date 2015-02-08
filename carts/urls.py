from django.conf.urls import url, patterns

import views

urlpatterns = patterns('',
    url(r'^add', views.CartCreateRest.as_view(), name='add'),
    url(r'^(?P<pk>[0-9]+)$', views.CartDetailView.as_view(), name='detail')
)
