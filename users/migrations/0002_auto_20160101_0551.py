# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-01 05:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email_address',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
