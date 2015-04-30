# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('ip', models.IPAddressField(blank=True, null=True)),
                ('user_agent', models.TextField(blank=True, max_length=100, null=True)),
                ('http_refferer', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('full_url', models.URLField(max_length=2000)),
                ('short_url', models.TextField(unique=True, max_length=10)),
                ('counter', models.BigIntegerField(default=0)),
                ('date', models.DateTimeField()),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='details',
            name='url_id',
            field=models.ForeignKey(to='url.Url'),
        ),
    ]
