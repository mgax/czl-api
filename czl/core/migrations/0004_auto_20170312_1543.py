# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-12 15:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20170312_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='url',
            field=models.URLField(max_length=2048),
        ),
    ]
