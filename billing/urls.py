from django.conf.urls import url, patterns

import views

urlpatterns = patterns('',
    url(r'^$', views.BillingView.as_view(), name='index')
)
