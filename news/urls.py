# -*- coding: utf-8 -*-

from django.conf.urls import *

from . import views


urlpatterns = [
    url(r'^', views.news_view, name='home')
]