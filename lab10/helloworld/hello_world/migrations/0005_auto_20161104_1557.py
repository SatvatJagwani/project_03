# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-04 10:27
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello_world', '0004_auto_20161101_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='endsem_exam_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 4, 15, 57, 5, 475000)),
        ),
        migrations.AlterField(
            model_name='course',
            name='midsem_exam_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 4, 15, 57, 5, 475000)),
        ),
        migrations.AlterField(
            model_name='feedbackform',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 4, 15, 57, 5, 491000)),
        ),
    ]
