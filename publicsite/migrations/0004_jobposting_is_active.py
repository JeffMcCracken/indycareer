# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-12-04 19:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicsite', '0003_jobposting'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobposting',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]