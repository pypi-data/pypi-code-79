# Generated by Django 2.2.16 on 2020-11-10 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0053_related_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='value_type',
            field=models.CharField(choices=[('text', 'Text'), ('url', 'URL'), ('integer', 'Integer'), ('float', 'Float'), ('boolean', 'Boolean'), ('datetime', 'Datetime'), ('option', 'Option'), ('file', 'File')], help_text='Type of value for this question.', max_length=8, verbose_name='Value type'),
        ),
        migrations.AlterField(
            model_name='question',
            name='widget_type',
            field=models.CharField(choices=[('text', 'Text'), ('textarea', 'Textarea'), ('yesno', 'Yes/No'), ('checkbox', 'Checkboxes'), ('radio', 'Radio buttons'), ('select', 'Select drop-down'), ('range', 'Range slider'), ('date', 'Date picker'), ('file', 'File upload')], help_text='Type of widget for this question.', max_length=12, verbose_name='Widget type'),
        ),
    ]
