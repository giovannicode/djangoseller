from django.conf.urls import url, patterns

import views

urlpatterns = patterns('',
    url(r'^add', views.CartCreateRest.as_view(), name='add'),
    url(r'^$', views.CartDetailView.as_view(), name='detail')
)
