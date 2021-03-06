# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-02 20:16
from __future__ import unicode_literals

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0005_userprofile_country'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='drop_location',
        ),
        migrations.RemoveField(
            model_name='order',
            name='drop_location_title',
        ),
        migrations.RemoveField(
            model_name='order',
            name='pick_up_location',
        ),
        migrations.RemoveField(
            model_name='order',
            name='receiver',
        ),
        migrations.RemoveField(
            model_name='order',
            name='sender',
        ),
        migrations.AddField(
            model_name='order',
            name='data',
            field=jsonfield.fields.JSONField(default=dict),
        ),
    ]
