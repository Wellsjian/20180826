# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-06-22 13:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='pub_date',
        ),
    ]
