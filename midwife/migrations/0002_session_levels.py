# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-05 08:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('midwife', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='session_levels',
            fields=[
                ('session_id', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('phonenumber', models.CharField(max_length=25, null=True)),
                ('level', models.IntegerField(null=True)),
            ],
        ),
    ]
