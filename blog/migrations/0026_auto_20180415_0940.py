# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-15 09:40
from __future__ import unicode_literals

import wagtail.core.blocks
import wagtail.core.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0025_auto_20180415_0835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='content',
            field=wagtail.core.fields.StreamField((('link_blocks', wagtail.core.blocks.StructBlock((('page', wagtail.core.blocks.PageChooserBlock(required=False)), ('url', wagtail.core.blocks.URLBlock(required=False)), ('content', wagtail.core.blocks.RichTextBlock())))),)),
        ),
    ]
