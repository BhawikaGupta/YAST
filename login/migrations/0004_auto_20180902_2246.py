# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-09-02 17:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_users_profile_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users_profile',
            name='CONTACT',
            field=models.CharField(max_length=100),
        ),
    ]
