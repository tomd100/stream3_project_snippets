# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-08 12:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscribe', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriptiontype',
            name='start_date',
            field=models.CharField(default='', max_length=10),
        ),
    ]