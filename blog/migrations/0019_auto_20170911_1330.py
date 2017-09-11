# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-11 13:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0018_auto_20170911_1313'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogcategory',
            name='icon',
        ),
        migrations.RemoveField(
            model_name='blogpagegalleryimage',
            name='image',
        ),
        migrations.RemoveField(
            model_name='blogpagegalleryimage',
            name='page',
        ),
        migrations.RemoveField(
            model_name='blogpage',
            name='categories',
        ),
        migrations.RemoveField(
            model_name='blogpage',
            name='intro',
        ),
        migrations.AddField(
            model_name='blogpage',
            name='heading',
            field=models.TextField(default='Heading'),
        ),
        migrations.AddField(
            model_name='blogpage',
            name='sub_heading',
            field=models.TextField(blank=True, default='Sub Heading'),
        ),
        migrations.AddField(
            model_name='blogpage',
            name='sub_sub_heading',
            field=models.TextField(blank=True, default='Sub Sub Heading'),
        ),
        migrations.DeleteModel(
            name='BlogCategory',
        ),
        migrations.DeleteModel(
            name='BlogPageGalleryImage',
        ),
    ]