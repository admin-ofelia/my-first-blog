# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-10-25 16:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Punto_de_venta', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='iva',
            field=models.IntegerField(),
        ),
    ]
