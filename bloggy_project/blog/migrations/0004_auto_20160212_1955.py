# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-12 19:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.CharField(max_length=128, unique=True),
        ),
    ]
