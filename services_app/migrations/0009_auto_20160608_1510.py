# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-08 15:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services_app', '0008_auto_20160607_1418'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vetsdisplay',
            old_name='published',
            new_name='published_slider',
        ),
        migrations.AddField(
            model_name='vetsdisplay',
            name='published_lasvets',
            field=models.BooleanField(default=True, verbose_name='Publicado'),
        ),
    ]
