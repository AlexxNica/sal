# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-31 11:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0006_auto_20161019_0813'),
    ]

    operations = [
        migrations.CreateModel(
            name='SearchFieldCache',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search_model', models.CharField(choices=[('Machine', 'Machine'), ('Facter', 'Facter'), ('Condition', 'Condition'), ('External Script', 'External Script')], default='AND', max_length=254, verbose_name='Search item')),
                ('search_field', models.CharField(max_length=254)),
            ],
        ),
        migrations.AlterModelOptions(
            name='searchgroup',
            options={'ordering': ['position']},
        ),
        migrations.AlterModelOptions(
            name='searchrow',
            options={'ordering': ['position']},
        ),
        migrations.AlterField(
            model_name='savedsearch',
            name='name',
            field=models.CharField(default='Unsaved Search 2016-10-31 11:05:54.671649+00:00', max_length=100),
        ),
        migrations.AlterField(
            model_name='searchrow',
            name='and_or',
            field=models.CharField(choices=[('AND', 'AND'), ('OR', 'OR')], default='AND', max_length=3, verbose_name='AND / OR'),
        ),
        migrations.AlterField(
            model_name='searchrow',
            name='position',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='searchrow',
            name='search_models',
            field=models.CharField(choices=[('Machine', 'Machine'), ('Facter', 'Facter'), ('Condition', 'Condition'), ('External Script', 'External Script')], default='AND', max_length=254, verbose_name='Search item'),
        ),
    ]
