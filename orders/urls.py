from django.conf.urls import url, patterns
import views

urlpatterns = patterns('',
    url(r'^$', views.OrderListView.as_view(), name='index'),
    url(r'^detail/(?P<pk>[0-9]+)$', views.OrderDetailView.as_view(), name='detail'),
)
