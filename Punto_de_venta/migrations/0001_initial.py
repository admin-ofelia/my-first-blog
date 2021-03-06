# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-10-14 19:46
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Caja',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CajaOperacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_apertura', models.DateTimeField(default=django.utils.timezone.now)),
                ('fecha_cierre', models.DateTimeField(default=django.utils.timezone.now)),
                ('saldo_inicial', models.DecimalField(decimal_places=2, max_digits=10)),
                ('saldo_final', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cajas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Punto_de_venta.Caja')),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('RFC', models.CharField(max_length=60)),
                ('clave', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefono', models.CharField(max_length=50)),
                ('correo', models.EmailField(max_length=75)),
                ('celular', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='DetalleVenta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.DecimalField(decimal_places=2, max_digits=10)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('iva', models.DecimalField(decimal_places=2, max_digits=10)),
                ('descuento', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('codigo_barras', models.CharField(max_length=30)),
                ('precio', models.IntegerField()),
                ('iva', models.CharField(max_length=5)),
                ('existencia', models.IntegerField()),
                ('dep', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Punto_de_venta.Departamento')),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Punto_de_venta.Marca')),
            ],
        ),
        migrations.CreateModel(
            name='Provedores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('clave', models.CharField(max_length=30)),
                ('contacto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Punto_de_venta.Contacto')),
            ],
        ),
        migrations.CreateModel(
            name='Ubicacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(max_length=40)),
                ('municipio', models.CharField(max_length=50)),
                ('ciudad', models.CharField(max_length=40)),
                ('calle', models.CharField(max_length=50)),
                ('No', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UnidadMedida',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_medida', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Ventas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('forma_de_pago', models.CharField(choices=[('01', 'EFECTIVO'), ('02', 'TRANSFERENCIA'), ('03', 'TARJETA')], default='01', max_length=2)),
                ('monto_pagado', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now)),
                ('subtotal', models.DecimalField(decimal_places=2, max_digits=10)),
                ('iva', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cambio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('caja', models.ManyToManyField(to='Punto_de_venta.Caja')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Punto_de_venta.Clientes')),
            ],
        ),
        migrations.AddField(
            model_name='provedores',
            name='ubicacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Punto_de_venta.Ubicacion'),
        ),
        migrations.AddField(
            model_name='productos',
            name='provedores',
            field=models.ManyToManyField(to='Punto_de_venta.Provedores'),
        ),
        migrations.AddField(
            model_name='productos',
            name='unidad_de_medida',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Punto_de_venta.UnidadMedida'),
        ),
        migrations.AddField(
            model_name='detalleventa',
            name='productos',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Punto_de_venta.Productos'),
        ),
        migrations.AddField(
            model_name='detalleventa',
            name='ventas',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Punto_de_venta.Ventas'),
        ),
        migrations.AddField(
            model_name='clientes',
            name='contacto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Punto_de_venta.Contacto'),
        ),
        migrations.AddField(
            model_name='clientes',
            name='ubicacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Punto_de_venta.Ubicacion'),
        ),
    ]
