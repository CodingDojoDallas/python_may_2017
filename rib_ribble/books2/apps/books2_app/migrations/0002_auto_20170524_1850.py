# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-24 18:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books2_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='published_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
