# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-28 19:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('election', '0002_kandydat_numer'),
    ]

    operations = [
        migrations.AddField(
            model_name='gmina',
            name='liczbaGlosowKand1',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gmina',
            name='liczbaGlosowKand2',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]