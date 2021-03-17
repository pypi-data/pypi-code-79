# Generated by Django 2.2.6 on 2019-10-29 12:08

from django.conf import settings
from django.db import migrations, models


def run_data_migration(apps, schema_editor):
    for element in apps.get_model('views', 'View').objects.all():
        element.uri_prefix = element.uri_prefix or settings.DEFAULT_URI_PREFIX
        element.save()


class Migration(migrations.Migration):

    dependencies = [
        ('views', '0016_django2'),
    ]

    operations = [
        migrations.RunPython(run_data_migration),
        migrations.AlterField(
            model_name='view',
            name='uri_prefix',
            field=models.URLField(help_text='The prefix for the URI of this view.', max_length=256, verbose_name='URI Prefix'),
        ),
    ]
