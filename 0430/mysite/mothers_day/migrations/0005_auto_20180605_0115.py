# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-04 17:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mothers_day', '0004_auto_20180605_0011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='message',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
