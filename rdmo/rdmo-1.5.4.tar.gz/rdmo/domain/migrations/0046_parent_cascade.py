# Generated by Django 2.2.13 on 2020-10-02 16:35

from django.db import migrations
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('domain', '0045_require_uri_prefix'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attribute',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, help_text='Parent attribute in the domain model.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='domain.Attribute', verbose_name='Parent attribute'),
        ),
    ]
