from django.conf.urls import url, patterns

import views

urlpatterns = patterns('',
    url(r'signup', views.UserCreateView.as_view(), name='signup')
)
