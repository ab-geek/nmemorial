# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-14 19:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_auto_20161114_1943'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentGallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('memorial_guid', models.IntegerField()),
                ('documentname', models.CharField(max_length=255)),
                ('documentlocation', models.CharField(max_length=255)),
            ],
        ),
    ]
