# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-12 19:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20160212_1730'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.CharField(default='test', max_length=128),
            preserve_default=False,
        ),
    ]
