# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-06 16:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0004_auto_20171106_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='kalendarz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.Calendar'),
        ),
    ]