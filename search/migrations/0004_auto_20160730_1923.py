# -*- coding: utf-8 -*-
# Generated by Django 1.10rc1 on 2016-07-30 19:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0003_auto_20160730_0217'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='board',
            name='board_votes',
        ),
        migrations.RemoveField(
            model_name='response',
            name='response_votes',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='tag_votes',
        ),
        migrations.AddField(
            model_name='board',
            name='like',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='response',
            name='like',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tag',
            name='like',
            field=models.BooleanField(default=False),
        ),
    ]
