# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-11 20:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subscribe', '0006_auto_20171210_0706'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subscription',
            old_name='name',
            new_name='type',
        ),
    ]
