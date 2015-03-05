from django.conf.urls import url, patterns

import views

urlpatterns = patterns('',
    url(r'^add', views.CartCreateRest.as_view(), name='add'),
    url(r'^detail$', views.CartDetailView.as_view(), name='detail')
    url(r'^delete/?P<pk>\d+/$',views.DetailView.as_view(), name='detail')
)
