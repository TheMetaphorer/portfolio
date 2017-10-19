# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

from .models import NewsUpdate

# Create your views here.


def news_view(request):
    news_posts = NewsUpdate.objects.all().order_by("-created")
    return render(request, 'news.html', {"news": news_posts})