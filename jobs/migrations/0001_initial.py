# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-12-10 19:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobPosting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('office', models.CharField(max_length=150)),
                ('status', models.CharField(max_length=150)),
                ('expectations', models.TextField()),
                ('requirements', models.TextField()),
                ('benefits', models.TextField()),
                ('details', models.TextField()),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Job Postings',
            },
        ),
    ]
