# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-20 15:54
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_versioning', '0007_auto_20180813_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='version',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
