# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-12-25 08:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mng_sys', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='files',
            name='slug',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]
