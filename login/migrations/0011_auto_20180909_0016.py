# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-09-08 18:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0010_active_campaigns'),
    ]

    operations = [
        migrations.AlterField(
            model_name='active_campaigns',
            name='DATE',
            field=models.DateField(max_length=100),
        ),
    ]