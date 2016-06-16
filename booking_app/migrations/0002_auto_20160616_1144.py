# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-16 11:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0002_logentry_remove_auto_add'),
        ('account', '0002_email_max_length'),
        ('socialaccount', '0003_extra_data_default_dict'),
        ('booking_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='booking',
            options={'verbose_name_plural': 'Reservas'},
        ),
        migrations.AlterModelOptions(
            name='pet',
            options={'verbose_name_plural': 'Mascotas'},
        ),
        migrations.RemoveField(
            model_name='booking',
            name='pet_customer',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='user_customer',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='user_veterian',
        ),
        migrations.RemoveField(
            model_name='pet',
            name='user_customer',
        ),
    ]