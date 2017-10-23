# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home_view, name='home'),
    url('r^contactus$', views.contact_us_view, name='contact'),
    url(r'^(?P<name>[a-z]+)$', views.member_view, name='members'),
]