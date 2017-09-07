# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-05 09:15
from __future__ import unicode_literals

import django.db.models.deletion
import modelcluster.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0008_auto_20170905_0858'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResumePageRelatedTextAndCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('text', models.TextField()),
                ('code', models.TextField()),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='resumepage',
            name='contact_me',
        ),
        migrations.AddField(
            model_name='resumepagerelatedtextandcode',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE,
                                                  related_name='related_links', to='blog.ResumePage'),
        ),
    ]
