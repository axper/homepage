# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-11 12:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0014_auto_20170907_1327'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resumepage',
            old_name='body',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='resumepage',
            old_name='name',
            new_name='heading',
        ),
    ]
