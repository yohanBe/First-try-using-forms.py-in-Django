# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-24 13:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formstest', '0004_auto_20160224_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogposts',
            name='name',
            field=models.CharField(max_length=15),
        ),
    ]
