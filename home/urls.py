# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<name>[a-z]+)$', views.member_view, name='members')
]