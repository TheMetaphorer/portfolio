# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.


class NewsUpdate(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created = models.DateField(default=timezone.now())
    by = models.CharField(max_length=32)

    def __str__(self):
        return self.title + " by " + self.by