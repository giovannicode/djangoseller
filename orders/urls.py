from django.conf.urls import url, patterns
import views

urlpatterns = patterns('',
    url(r'^$', views.OrderListView.as_view(), name='index'),
)
