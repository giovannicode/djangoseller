from django.conf.urls import url, patterns

import views

urlpatterns = patterns('',
    url(r'^create/', views.ReviewCreateView.as_view(), name='create'),
)
