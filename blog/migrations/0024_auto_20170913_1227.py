# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-13 12:27
from __future__ import unicode_literals

import wagtail.core.blocks
import wagtail.core.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0023_auto_20170913_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='content',
            field=wagtail.core.fields.StreamField((('link_blocks', wagtail.core.blocks.StructBlock(((
                                                                                                                  'page',
                                                                                                                  wagtail.core.blocks.PageChooserBlock()),
                                                                                                    (
                                                                                                                  'content',
                                                                                                                  wagtail.core.blocks.RichTextBlock())))),)),
        ),
    ]