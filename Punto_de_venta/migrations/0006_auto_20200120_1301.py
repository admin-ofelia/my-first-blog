# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-01-20 19:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Punto_de_venta', '0005_detalleventa_importe'),
    ]

    operations = [
        migrations.AddField(
            model_name='cajaoperacion',
            name='status',
            field=models.CharField(default=0, max_length=1),
        ),
        migrations.AlterField(
            model_name='cajaoperacion',
            name='fecha_apertura',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cajaoperacion',
            name='saldo_final',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='cajaoperacion',
            name='saldo_inicial',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
