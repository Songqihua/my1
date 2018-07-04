# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-02 19:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0012_auto_20180630_2131'),
    ]

    operations = [
        migrations.CreateModel(
            name='Citys',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('upid', models.IntegerField()),
            ],
            options={
                'db_table': 'citys',
            },
        ),
        migrations.AlterField(
            model_name='goods',
            name='typeid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myadmin.Classify'),
        ),
    ]
