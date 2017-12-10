# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-10 07:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subscribe', '0005_auto_20171209_1612'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderLineItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subscribe.Order')),
            ],
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('description', models.CharField(default='', max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.RemoveField(
            model_name='subscriptionordered',
            name='order',
        ),
        migrations.RemoveField(
            model_name='subscriptionordered',
            name='subscription',
        ),
        migrations.DeleteModel(
            name='SubscriptionOrdered',
        ),
        migrations.DeleteModel(
            name='SubscriptionType',
        ),
        migrations.AddField(
            model_name='orderlineitem',
            name='subscription',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subscribe.Subscription'),
        ),
    ]