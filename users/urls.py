from django.conf.urls import url, patterns

import views

urlpatterns = patterns('',
    url(r'signup', views.UserCreateView.as_view(), name='signup'),
    url(r'signin', views.UserLoginView.as_view(), name='signin'),
    url(r'signout', views.signout, name='signout'),
    url(r'forgot-password', views.ForgotPasswordView.as_view(), name='forgot-password')
)
