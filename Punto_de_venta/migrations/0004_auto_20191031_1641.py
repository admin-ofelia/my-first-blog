# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-10-31 22:41
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Punto_de_venta', '0003_auto_20191031_1628'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='caja',
            name='empleado',
        ),
        migrations.AddField(
            model_name='ventas',
            name='empleado',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]