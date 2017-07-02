# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-02 15:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_auto_20170702_1707'),
    ]

    operations = [
        migrations.AddField(
            model_name='cars',
            name='name',
            field=models.CharField(default=None, max_length=250, verbose_name='Nom'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cars',
            name='year',
            field=models.IntegerField(default=None),
            preserve_default=False,
        ),
    ]