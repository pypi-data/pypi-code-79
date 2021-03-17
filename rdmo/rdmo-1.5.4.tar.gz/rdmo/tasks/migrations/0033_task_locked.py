# Generated by Django 2.2.16 on 2021-01-22 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0032_task_catalogs'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='locked',
            field=models.BooleanField(default=False, help_text='Designates whether this task can be changed.', verbose_name='Locked'),
        ),
    ]
