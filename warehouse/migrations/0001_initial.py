# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-22 17:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Arrival',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Arrival Date')),
                ('bestBefore', models.DateField(blank=True, null=True, verbose_name='Best Before')),
                ('price', models.DecimalField(decimal_places=2, max_digits=16, verbose_name='Price')),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=16, verbose_name='Qty Arrived')),
                ('inStock', models.DecimalField(decimal_places=2, max_digits=16, verbose_name='Qty In Stock')),
            ],
            options={
                'verbose_name': 'Product arrival',
                'verbose_name_plural': 'Product arrivals',
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254, verbose_name='Contact Name')),
                ('address', models.TextField(verbose_name='Address')),
                ('phone', models.CharField(max_length=254, verbose_name='Contact Phone')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='E-mail')),
                ('comment', models.TextField(verbose_name='Comment')),
            ],
            options={
                'verbose_name': 'Company',
                'verbose_name_plural': 'Companies',
            },
        ),
        migrations.CreateModel(
            name='Dispatch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Dispatch Date')),
                ('price', models.DecimalField(decimal_places=2, max_digits=16, verbose_name='Price')),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=16, verbose_name='Qty Dispatched')),
                ('distributor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='warehouse.Company')),
            ],
            options={
                'verbose_name': 'Dispatch',
                'verbose_name_plural': 'Dispatches',
            },
        ),
        migrations.CreateModel(
            name='Lot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=16, verbose_name='Qty Dispatched')),
                ('arrival', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='warehouse.Arrival')),
                ('dispatch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='warehouse.Dispatch')),
            ],
            options={
                'verbose_name': 'Lot',
                'verbose_name_plural': 'Lots',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254, verbose_name='Product Name')),
                ('unit', models.CharField(max_length=16, verbose_name='Measurment unit')),
                ('image',
                 models.ImageField(blank=True, null=True, upload_to='img/products/', verbose_name='Product Image')),
                ('inStock', models.DecimalField(decimal_places=2, max_digits=16, verbose_name='Qty in stock')),
                ('description', models.TextField(verbose_name='Description of product')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.AddField(
            model_name='dispatch',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='warehouse.Product'),
        ),
        migrations.AddField(
            model_name='arrival',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='warehouse.Product'),
        ),
        migrations.AddField(
            model_name='arrival',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='warehouse.Company'),
        ),
    ]
