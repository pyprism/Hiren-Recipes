# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-20 08:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0008_auto_20170413_1936'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='tips',
            field=models.TextField(blank=True, null=True),
        ),
    ]
