from django.conf.urls import url, patterns

import views

urlpatterns = patterns('',
    url(r'^$', views.AccountView.as_view(), name='index')
)
