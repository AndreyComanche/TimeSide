# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-04 14:49
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('server', '0010_auto_20160928_0014'),
    ]

    operations = [
        migrations.AddField(
            model_name='annotation',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='annotation', to=settings.AUTH_USER_MODEL, verbose_name='author'),
        ),
        migrations.AddField(
            model_name='annotation',
            name='is_public',
            field=models.BooleanField(default=True),
        ),
    ]
