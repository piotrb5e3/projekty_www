# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-28 21:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('election', '0003_auto_20160328_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gmina',
            name='wojewodztwo',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='election.Wojewodztwo'),
        ),
    ]
