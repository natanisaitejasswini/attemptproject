# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-23 16:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0005_auto_20160822_2215'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userlog',
            name='alias',
        ),
    ]