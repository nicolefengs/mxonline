# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-04-27 15:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='age',
            field=models.IntegerField(default=18, verbose_name='\u5e74\u9f84'),
        ),
    ]