# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2018-06-05 06:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('byond_app', '0002_auto_20180605_0635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_name',
            field=models.CharField(default='Article name', max_length=255),
        ),
    ]