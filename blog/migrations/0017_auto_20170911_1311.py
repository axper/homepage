# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-11 13:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0016_auto_20170911_1308'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogindexpage',
            name='heading',
            field=models.TextField(default='Heading'),
        ),
        migrations.AddField(
            model_name='blogindexpage',
            name='sub_heading',
            field=models.TextField(default='Sub Heading'),
        ),
        migrations.AddField(
            model_name='blogindexpage',
            name='sub_sub_heading',
            field=models.TextField(default='Sub Sub Heading'),
        ),
    ]
