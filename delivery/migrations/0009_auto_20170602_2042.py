# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-02 20:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0008_order_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='geo_drop',
        ),
        migrations.RemoveField(
            model_name='order',
            name='geo_pickup',
        ),
    ]