# -*- coding: utf-8 -*-
# Generated by Django 1.10rc1 on 2016-07-30 02:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0002_auto_20160729_2142'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='board_icon',
            field=models.FileField(default='none', upload_to=b''),
        ),
        migrations.AddField(
            model_name='response',
            name='image',
            field=models.FileField(default='none', upload_to=b''),
        ),
    ]