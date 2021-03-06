# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-07 13:27
from __future__ import unicode_literals

import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0013_auto_20170907_0908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resumepage',
            name='body',
            field=wagtail.core.fields.StreamField((('section_block', wagtail.core.blocks.StructBlock(((
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
                                                                                                                            blank=True)),
                                                                                                                        (
                                                                                                                        'description_list_block',
                                                                                                                        wagtail.core.blocks.StructBlock(
                                                                                                                            (
                                                                                                                            (
                                                                                                                            'content',
                                                                                                                            wagtail.core.blocks.StreamBlock(
                                                                                                                                (
                                                                                                                                (
                                                                                                                                'description_item_block',
                                                                                                                                wagtail.core.blocks.StructBlock(
                                                                                                                                    (
                                                                                                                                    (
                                                                                                                                    'data_title',
                                                                                                                                    wagtail.core.blocks.CharBlock()),
                                                                                                                                    (
                                                                                                                                    'data_definition',
                                                                                                                                    wagtail.core.blocks.CharBlock())))),))),),
                                                                                                                            blank=True)),
                                                                                                                        (
                                                                                                                        'download_button_block',
                                                                                                                        wagtail.core.blocks.StructBlock(
                                                                                                                            (
                                                                                                                            (
                                                                                                                            'url',
                                                                                                                            wagtail.core.blocks.URLBlock()),
                                                                                                                            (
                                                                                                                            'text',
                                                                                                                            wagtail.core.blocks.CharBlock())),
                                                                                                                            blank=True)),
                                                                                                                        (
                                                                                                                        'h3_section_block',
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
                                                                                                                                    blank=True)),
                                                                                                                                (
                                                                                                                                'description_list_block',
                                                                                                                                wagtail.core.blocks.StructBlock(
                                                                                                                                    (
                                                                                                                                    (
                                                                                                                                    'content',
                                                                                                                                    wagtail.core.blocks.StreamBlock(
                                                                                                                                        (
                                                                                                                                        (
                                                                                                                                        'description_item_block',
                                                                                                                                        wagtail.core.blocks.StructBlock(
                                                                                                                                            (
                                                                                                                                            (
                                                                                                                                            'data_title',
                                                                                                                                            wagtail.core.blocks.CharBlock()),
                                                                                                                                            (
                                                                                                                                            'data_definition',
                                                                                                                                            wagtail.core.blocks.CharBlock())))),))),),
                                                                                                                                    blank=True)),
                                                                                                                                (
                                                                                                                                'download_button_block',
                                                                                                                                wagtail.core.blocks.StructBlock(
                                                                                                                                    (
                                                                                                                                    (
                                                                                                                                    'url',
                                                                                                                                    wagtail.core.blocks.URLBlock()),
                                                                                                                                    (
                                                                                                                                    'text',
                                                                                                                                    wagtail.core.blocks.CharBlock())),
                                                                                                                                    blank=True)),
                                                                                                                                (
                                                                                                                                'h4_section_block',
                                                                                                                                wagtail.core.blocks.StructBlock(
                                                                                                                                    (
                                                                                                                                    (
                                                                                                                                    'id',
                                                                                                                                    wagtail.core.blocks.CharBlock(
                                                                                                                                        required=False)),
                                                                                                                                    (
                                                                                                                                    'title',
                                                                                                                                    wagtail.core.blocks.CharBlock())))))))))))))))),),
                                                  blank=True),
        ),
    ]
