__author__ = 'jxl'
from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'pinlist.views.home', name='home'),
    url(r'^login/$', 'django.contrib.auth.views.login',
        {'template_name': 'pinlist/login.html'}, name='login'),
    url(r'^register/$', 'pinlist.views.register', name='register'),
    url(r'^logout/$', 'pinlist.views.logout_user', name='logout'),
)