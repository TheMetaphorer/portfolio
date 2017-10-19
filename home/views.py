# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from home.models import Member

# Create your views here.


def member_view(request, **kwargs):
    request_member = Member.objects.get(name=kwargs['name'])
    return render(request, "member.html", {"member": request_member})


def contact_us_view(request):
    return render(request, 'contact_us.html')
