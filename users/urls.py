from django.conf.urls import url, patterns

import views

urlpatterns = patterns('',
    url(r'signup', views.UserCreateView.as_view(), name='signup'),
    url(r'signin', views.UserLoginView.as_view(), name='signin'),
    url(r'signout', views.signout, name='signout'),
    url(r'forgot-password', views.ForgotPasswordView.as_view(), name='forgot-password'),
    url(
        r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.ResetPasswordView.as_view(),
        name='password_reset_confirm'
    ),
)
