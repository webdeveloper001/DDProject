# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-22 20:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0012_auto_20170612_1417'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='track',
            name='action',
        ),
        migrations.RemoveField(
            model_name='track',
            name='address1',
        ),
        migrations.RemoveField(
            model_name='track',
            name='location1',
        ),
        migrations.RemoveField(
            model_name='track',
            name='location2',
        ),
        migrations.RemoveField(
            model_name='track',
            name='next_user',
        ),
        migrations.RemoveField(
            model_name='track',
            name='ordernum',
        ),
        migrations.RemoveField(
            model_name='track',
            name='status',
        ),
    ]