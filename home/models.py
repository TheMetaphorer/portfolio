# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Member(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    bio = models.TextField()
    img_url = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return unicode(self.name)