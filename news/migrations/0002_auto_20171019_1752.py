# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-19 17:52
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsupdate',
            name='created',
            field=models.DateField(default=datetime.datetime(2017, 10, 19, 17, 52, 16, 165263, tzinfo=utc)),
        ),
    ]
