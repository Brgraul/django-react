# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-20 15:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_booking', '0008_auto_20160720_1319'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='levelone',
            name='level',
        ),
        migrations.RemoveField(
            model_name='levelthree',
            name='level',
        ),
        migrations.RemoveField(
            model_name='leveltwo',
            name='level',
        ),
        migrations.AddField(
            model_name='booking',
            name='pet',
            field=models.ManyToManyField(to='app_booking.Pet'),
        ),
        migrations.DeleteModel(
            name='LevelOne',
        ),
        migrations.DeleteModel(
            name='LevelThree',
        ),
        migrations.DeleteModel(
            name='LevelTwo',
        ),
        migrations.DeleteModel(
            name='TopLevel',
        ),
    ]