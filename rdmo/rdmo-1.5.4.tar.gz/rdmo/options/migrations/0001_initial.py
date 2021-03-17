# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-21 10:28
from __future__ import unicode_literals

import rdmo.core.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('domain', '0019_meta'),
    ]

    operations = [
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, validators=[django.core.validators.RegexValidator('^[a-zA-z0-9_]*$', 'Only letters, numbers, or underscores are allowed.')])),
                ('order', models.IntegerField(null=True)),
                ('text_en', models.CharField(max_length=256)),
                ('text_de', models.CharField(max_length=256)),
                ('additional_input', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('optionset', 'order'),
                'verbose_name': 'Option',
                'verbose_name_plural': 'Options',
            },
            bases=(models.Model, rdmo.core.models.TranslationMixin),
        ),
        migrations.CreateModel(
            name='OptionSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, validators=[django.core.validators.RegexValidator('^[a-zA-z0-9_]*$', 'Only letters, numbers, or underscores are allowed.')])),
                ('order', models.IntegerField(null=True)),
            ],
            options={
                'ordering': ('title', ),
                'verbose_name': 'OptionSet',
                'verbose_name_plural': 'OptionSets',
            },
        ),
        migrations.AddField(
            model_name='option',
            name='optionset',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='options', to='options.OptionSet'),
        ),
    ]
