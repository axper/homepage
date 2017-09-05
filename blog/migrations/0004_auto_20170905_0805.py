# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-05 08:05
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20170905_0802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resumepage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField((('person', wagtail.wagtailcore.blocks.StructBlock((('name', wagtail.wagtailcore.blocks.CharBlock()), ('height', wagtail.wagtailcore.blocks.DecimalBlock()), ('age', wagtail.wagtailcore.blocks.DecimalBlock())))),)),
        ),
    ]
