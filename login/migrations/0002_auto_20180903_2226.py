# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-09-03 16:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users_profile',
            name='LATITUDE',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='users_profile',
            name='LONGITUDE',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]