# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-07 09:08
from __future__ import unicode_literals

import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0012_auto_20170907_0836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resumepage',
            name='body',
            field=wagtail.core.fields.StreamField((('h2_section_block', wagtail.core.blocks.StructBlock(((
                                                                                                                       'id',
                                                                                                                       wagtail.core.blocks.CharBlock(
                                                                                                                           required=False)),
                                                                                                         (
                                                                                                                       'title',
                                                                                                                       wagtail.core.blocks.CharBlock()),
                                                                                                         (
                                                                                                                       'content',
                                                                                                                       wagtail.core.blocks.StreamBlock(
                                                                                                                           (
                                                                                                                           (
                                                                                                                           'rich_text',
                                                                                                                           wagtail.core.blocks.RichTextBlock(
                                                                                                                               blank=True)),
                                                                                                                           (
                                                                                                                           'h3_block',
                                                                                                                           wagtail.core.blocks.StructBlock(
                                                                                                                               (
                                                                                                                               (
                                                                                                                               'id',
                                                                                                                               wagtail.core.blocks.CharBlock(
                                                                                                                                   required=False)),
                                                                                                                               (
                                                                                                                               'title',
                                                                                                                               wagtail.core.blocks.CharBlock()),
                                                                                                                               (
                                                                                                                               'content',
                                                                                                                               wagtail.core.blocks.StreamBlock(
                                                                                                                                   (
                                                                                                                                   (
                                                                                                                                   'rich_text',
                                                                                                                                   wagtail.core.blocks.RichTextBlock(
                                                                                                                                       blank=True)),
                                                                                                                                   (
                                                                                                                                   'h4_block',
                                                                                                                                   wagtail.core.blocks.StructBlock(
                                                                                                                                       (
                                                                                                                                       (
                                                                                                                                       'id',
                                                                                                                                       wagtail.core.blocks.CharBlock(
                                                                                                                                           required=False)),
                                                                                                                                       (
                                                                                                                                       'title',
                                                                                                                                       wagtail.core.blocks.CharBlock()),
                                                                                                                                       (
                                                                                                                                       'content',
                                                                                                                                       wagtail.core.blocks.StreamBlock(
                                                                                                                                           (
                                                                                                                                           (
                                                                                                                                           'rich_text',
                                                                                                                                           wagtail.core.blocks.RichTextBlock(
                                                                                                                                               blank=True)),)))),
                                                                                                                                       blank=True)))))),
                                                                                                                               blank=True)),
                                                                                                                           (
                                                                                                                           'small_grid_block',
                                                                                                                           wagtail.core.blocks.StructBlock(
                                                                                                                               (
                                                                                                                               (
                                                                                                                               'dividend',
                                                                                                                               wagtail.core.blocks.IntegerBlock(
                                                                                                                                   default=1)),
                                                                                                                               (
                                                                                                                               'divisor',
                                                                                                                               wagtail.core.blocks.IntegerBlock(
                                                                                                                                   default=2)),
                                                                                                                               (
                                                                                                                               'content',
                                                                                                                               wagtail.core.blocks.StreamBlock(
                                                                                                                                   (
                                                                                                                                   (
                                                                                                                                   'card_block',
                                                                                                                                   wagtail.core.blocks.StructBlock(
                                                                                                                                       (
                                                                                                                                       (
                                                                                                                                       'id',
                                                                                                                                       wagtail.core.blocks.CharBlock(
                                                                                                                                           required=False)),
                                                                                                                                       (
                                                                                                                                       'title',
                                                                                                                                       wagtail.core.blocks.CharBlock()),
                                                                                                                                       (
                                                                                                                                       'link',
                                                                                                                                       wagtail.core.blocks.URLBlock()),
                                                                                                                                       (
                                                                                                                                       'image',
                                                                                                                                       wagtail.images.blocks.ImageChooserBlock()),
                                                                                                                                       (
                                                                                                                                       'content',
                                                                                                                                       wagtail.core.blocks.RichTextBlock())),
                                                                                                                                       blank=True)),)))),
                                                                                                                               blank=True)))))))),
                                                   ('small_grid_block', wagtail.core.blocks.StructBlock(((
                                                                                                                       'dividend',
                                                                                                                       wagtail.core.blocks.IntegerBlock(
                                                                                                                           default=1)),
                                                                                                         (
                                                                                                                       'divisor',
                                                                                                                       wagtail.core.blocks.IntegerBlock(
                                                                                                                           default=2)),
                                                                                                         (
                                                                                                                       'content',
                                                                                                                       wagtail.core.blocks.StreamBlock(
                                                                                                                           (
                                                                                                                           (
                                                                                                                           'card_block',
                                                                                                                           wagtail.core.blocks.StructBlock(
                                                                                                                               (
                                                                                                                               (
                                                                                                                               'id',
                                                                                                                               wagtail.core.blocks.CharBlock(
                                                                                                                                   required=False)),
                                                                                                                               (
                                                                                                                               'title',
                                                                                                                               wagtail.core.blocks.CharBlock()),
                                                                                                                               (
                                                                                                                               'link',
                                                                                                                               wagtail.core.blocks.URLBlock()),
                                                                                                                               (
                                                                                                                               'image',
                                                                                                                               wagtail.images.blocks.ImageChooserBlock()),
                                                                                                                               (
                                                                                                                               'content',
                                                                                                                               wagtail.core.blocks.RichTextBlock())),
                                                                                                                               blank=True)),))))))),
                                                  blank=True),
        ),
    ]
