# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-12-10 19:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publicsite', '0004_jobposting_is_active'),
    ]

    operations = [
        migrations.RenameField(
            model_name='staff',
            old_name='position',
            new_name='order',
        ),
    ]