# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-08 22:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InApp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True)),
                ('product_id', models.CharField(default='', max_length=255)),
                ('transaction_id', models.IntegerField(blank=True)),
                ('original_transaction_id', models.IntegerField(blank=True)),
                ('purchase_date', models.CharField(default='', max_length=255)),
                ('purchase_date_ms', models.IntegerField(blank=True)),
                ('purchase_date_pst', models.CharField(default='', max_length=255)),
                ('original_purchase_date', models.CharField(default='', max_length=255)),
                ('original_purchase_date_ms', models.IntegerField(blank=True)),
                ('original_purchase_date_pst', models.CharField(default='', max_length=255)),
                ('is_trial_period', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_id', models.IntegerField(blank=True)),
                ('product_id', models.IntegerField(blank=True)),
                ('quantity', models.IntegerField(default=0)),
                ('purchased_at', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receipt_type', models.CharField(default='', max_length=255)),
                ('adam_id', models.IntegerField(blank=True)),
                ('app_item_id', models.IntegerField(blank=True)),
                ('bundle_id', models.CharField(default='', max_length=255)),
                ('application_version', models.CharField(default='', max_length=255)),
                ('download_id', models.IntegerField(blank=True)),
                ('version_external_identifier', models.IntegerField(blank=True)),
                ('receipt_creation_date', models.CharField(default='', max_length=255)),
                ('receipt_creation_date_ms', models.IntegerField(blank=True)),
                ('receipt_creation_date_pst', models.CharField(default='', max_length=255)),
                ('request_date', models.CharField(default='', max_length=255)),
                ('request_date_ms', models.IntegerField(blank=True)),
                ('request_date_pst', models.CharField(default='', max_length=255)),
                ('original_purchase_date', models.CharField(default='', max_length=255)),
                ('original_purchase_date_ms', models.IntegerField(blank=True)),
                ('original_purchase_date_pst', models.CharField(default='', max_length=255)),
                ('original_application_version', models.CharField(default='', max_length=255)),
                ('in_app', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='storekit.InApp')),
            ],
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(blank=True)),
                ('environment', models.CharField(default='', max_length=255)),
                ('receipt', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='storekit.Receipt')),
            ],
        ),
        migrations.AddField(
            model_name='purchase',
            name='response',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='storekit.Response'),
        ),
    ]
