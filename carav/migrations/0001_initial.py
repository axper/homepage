# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-08-12 17:18
from __future__ import unicode_literals

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WaterFountain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('lat', models.FloatField(verbose_name='Latitude')),
                ('lng', models.FloatField(verbose_name='Longitude')),
                ('deleted', models.BooleanField(default=False)),
            ],
        ),
    ]
