# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-12-10 21:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=150)),
                ('street', models.CharField(max_length=150)),
                ('zip_code', models.PositiveIntegerField()),
                ('phone', models.PositiveIntegerField()),
                ('exp_agent_goal', models.PositiveIntegerField(blank=True, null=True)),
                ('exp_agents', models.PositiveIntegerField(blank=True, null=True)),
                ('new_agent_goal', models.PositiveIntegerField(blank=True, null=True)),
                ('new_agents', models.PositiveIntegerField(blank=True, null=True)),
                ('agent_departures', models.PositiveIntegerField(blank=True, null=True)),
                ('team_departures', models.PositiveIntegerField(blank=True, null=True)),
                ('company_dollar', models.PositiveIntegerField(blank=True, null=True)),
            ],
        ),
    ]