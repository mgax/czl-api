# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-12 14:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_load_institutions'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='document',
            options={'ordering': ['-_created_at']},
        ),
        migrations.AlterModelOptions(
            name='publication',
            options={'ordering': ['-_created_at']},
        ),
        migrations.RenameField(
            model_name='document',
            old_name='submitted_by',
            new_name='_created_by',
        ),
        migrations.RenameField(
            model_name='publication',
            old_name='submitted_by',
            new_name='_created_by',
        ),
        migrations.AddField(
            model_name='document',
            name='_created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='publication',
            name='_created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
