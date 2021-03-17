# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-21 13:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0021_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='value',
            name='attribute',
            field=models.ForeignKey(blank=True, help_text='The attribute this value belongs to.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='values', to='domain.AttributeEntity', verbose_name='Attribute'),
        ),
    ]
