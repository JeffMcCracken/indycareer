# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-12-10 21:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_auto_20181210_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobposting',
            name='office',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_postings', to='reporting.Office'),
        ),
    ]
