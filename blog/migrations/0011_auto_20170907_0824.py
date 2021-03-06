# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-07 08:24
from __future__ import unicode_literals

import wagtail.core.blocks
import wagtail.core.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0010_auto_20170907_0713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resumepage',
            name='body',
            field=wagtail.core.fields.StreamField((('section', wagtail.core.blocks.StructBlock((('id',
                                                                                                 wagtail.core.blocks.CharBlock(
                                                                                                                   blank=True)),
                                                                                                (
                                                                                                              'content',
                                                                                                              wagtail.core.blocks.RichTextBlock(
                                                                                                                  blank=True)),
                                                                                                (
                                                                                                              'sub_section',
                                                                                                              wagtail.core.blocks.StructBlock(
                                                                                                                  ((
                                                                                                                   'id',
                                                                                                                   wagtail.core.blocks.CharBlock(
                                                                                                                       blank=True)),
                                                                                                                   (
                                                                                                                   'title',
                                                                                                                   wagtail.core.blocks.CharBlock()),
                                                                                                                   (
                                                                                                                   'content',
                                                                                                                   wagtail.core.blocks.RichTextBlock(
                                                                                                                       blank=True)),
                                                                                                                   (
                                                                                                                   'sub_section',
                                                                                                                   wagtail.core.blocks.StructBlock(
                                                                                                                       (
                                                                                                                       (
                                                                                                                       'id',
                                                                                                                       wagtail.core.blocks.CharBlock(
                                                                                                                           blank=True)),
                                                                                                                       (
                                                                                                                       'title',
                                                                                                                       wagtail.core.blocks.CharBlock()),
                                                                                                                       (
                                                                                                                       'content',
                                                                                                                       wagtail.core.blocks.RichTextBlock(
                                                                                                                           blank=True))),
                                                                                                                       blank=True))),
                                                                                                                  blank=True))))),),
                                                  blank=True),
        ),
    ]
