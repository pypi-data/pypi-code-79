# Generated by Django 2.2.12 on 2021-01-19 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0018_delinquent_flag_and_event_log_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='delinquent',
            field=models.BooleanField(db_index=True, default=True),
        ),
    ]
