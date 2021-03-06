# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-08-12 18:56
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
        ('blog', '0031_blogindex_banner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Map',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('banner', models.ImageField(blank=True, upload_to='')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
