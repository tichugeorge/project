# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-25 07:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='profilepic',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='media/sample_img/'),
            preserve_default=False,
        ),
    ]