# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-01-26 16:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0006_auto_20160803_1619'),
    ]

    operations = [
        migrations.AddField(
            model_name='catalog',
            name='comment',
            field=models.TextField(blank=True, help_text='Additional information about this catalog.', null=True, verbose_name='Comment'),
        ),
        migrations.AddField(
            model_name='catalog',
            name='key',
            field=models.SlugField(blank=True, help_text='The internal identifier of this catalog. The URI will be generated from this key.', max_length=128, null=True, verbose_name='Key'),
        ),
        migrations.AddField(
            model_name='catalog',
            name='uri',
            field=models.URLField(blank=True, help_text='The Uniform Resource Identifier of this catalog (auto-generated).', max_length=640, null=True, verbose_name='URI'),
        ),
        migrations.AddField(
            model_name='catalog',
            name='uri_prefix',
            field=models.URLField(blank=True, help_text='The prefix for the URI of this catalog.', max_length=256, null=True, verbose_name='URI Prefix'),
        ),
        migrations.AddField(
            model_name='questionentity',
            name='comment',
            field=models.TextField(blank=True, help_text='Additional information about this question/questionset.', null=True, verbose_name='Comment'),
        ),
        migrations.AddField(
            model_name='questionentity',
            name='key',
            field=models.SlugField(blank=True, help_text='The internal identifier of this question/questionset. The URI will be generated from this key.', max_length=128, null=True, verbose_name='Key'),
        ),
        migrations.AddField(
            model_name='questionentity',
            name='uri',
            field=models.URLField(blank=True, help_text='The Uniform Resource Identifier of this question/questionset (auto-generated).', max_length=640, null=True, verbose_name='URI'),
        ),
        migrations.AddField(
            model_name='questionentity',
            name='uri_prefix',
            field=models.URLField(blank=True, help_text='The prefix for the URI of this question/questionset.', max_length=256, null=True, verbose_name='URI Prefix'),
        ),
        migrations.AddField(
            model_name='section',
            name='comment',
            field=models.TextField(blank=True, help_text='Additional information about this section.', null=True, verbose_name='Comment'),
        ),
        migrations.AddField(
            model_name='section',
            name='key',
            field=models.SlugField(blank=True, help_text='The internal identifier of this section. The URI will be generated from this key.', max_length=128, null=True, verbose_name='Key'),
        ),
        migrations.AddField(
            model_name='section',
            name='uri',
            field=models.URLField(blank=True, help_text='The Uniform Resource Identifier of this section (auto-generated).', max_length=640, null=True, verbose_name='URI'),
        ),
        migrations.AddField(
            model_name='section',
            name='uri_prefix',
            field=models.URLField(blank=True, help_text='The prefix for the URI of this section.', max_length=256, null=True, verbose_name='URI Prefix'),
        ),
        migrations.AddField(
            model_name='subsection',
            name='comment',
            field=models.TextField(blank=True, help_text='Additional information about this subsection.', null=True, verbose_name='Comment'),
        ),
        migrations.AddField(
            model_name='subsection',
            name='key',
            field=models.SlugField(blank=True, help_text='The internal identifier of this subsection. The URI will be generated from this key.', max_length=128, null=True, verbose_name='Key'),
        ),
        migrations.AddField(
            model_name='subsection',
            name='uri',
            field=models.URLField(blank=True, help_text='The Uniform Resource Identifier of this subsection (auto-generated).', max_length=640, null=True, verbose_name='URI'),
        ),
        migrations.AddField(
            model_name='subsection',
            name='uri_prefix',
            field=models.URLField(blank=True, help_text='The prefix for the URI of this subsection.', max_length=256, null=True, verbose_name='URI Prefix'),
        ),
        migrations.AlterField(
            model_name='catalog',
            name='order',
            field=models.IntegerField(default=0, help_text='The position of this catalog in lists.', verbose_name='Order'),
        ),
        migrations.AlterField(
            model_name='catalog',
            name='title_de',
            field=models.CharField(help_text='The German title for this catalog.', max_length=256, verbose_name='Title (de)'),
        ),
        migrations.AlterField(
            model_name='catalog',
            name='title_en',
            field=models.CharField(help_text='The English title for this catalog.', max_length=256, verbose_name='Title (en)'),
        ),
        migrations.AlterField(
            model_name='question',
            name='parent',
            field=models.ForeignKey(blank=True, help_text='The question set this question belongs to.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='questions.QuestionEntity', verbose_name='Parent'),
        ),
        migrations.AlterField(
            model_name='question',
            name='text_de',
            field=models.TextField(help_text='The German text for this question.', verbose_name='Text (de)'),
        ),
        migrations.AlterField(
            model_name='question',
            name='text_en',
            field=models.TextField(help_text='The English text for this question.', verbose_name='Text (en)'),
        ),
        migrations.AlterField(
            model_name='question',
            name='widget_type',
            field=models.CharField(choices=[('text', 'Text'), ('textarea', 'Textarea'), ('yesno', 'Yes/No'), ('checkbox', 'Checkboxes'), ('radio', 'Radio buttons'), ('select', 'Select drop-down'), ('range', 'Range slider'), ('date', 'Date picker')], help_text='Type of widget for this question.', max_length=12, verbose_name='Widget type'),
        ),
        migrations.AlterField(
            model_name='questionentity',
            name='attribute_entity',
            field=models.ForeignKey(blank=True, help_text='The attribute/entity this question belongs to.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='domain.AttributeEntity', verbose_name='Attribute entity'),
        ),
        migrations.AlterField(
            model_name='questionentity',
            name='help_de',
            field=models.TextField(blank=True, help_text='The German help text for this question/questionset.', null=True, verbose_name='Help (de)'),
        ),
        migrations.AlterField(
            model_name='questionentity',
            name='help_en',
            field=models.TextField(blank=True, help_text='The English help text for this question/questionset.', null=True, verbose_name='Help (en)'),
        ),
        migrations.AlterField(
            model_name='questionentity',
            name='label_de',
            field=models.TextField(help_text='The German label for this question/questionset (auto-generated).', verbose_name='Label (de)'),
        ),
        migrations.AlterField(
            model_name='questionentity',
            name='label_en',
            field=models.TextField(help_text='The English label for this question/questionset (auto-generated).', verbose_name='Label (en)'),
        ),
        migrations.AlterField(
            model_name='questionentity',
            name='order',
            field=models.IntegerField(default=0, help_text='The position of this subsection in lists.', verbose_name='Order'),
        ),
        migrations.AlterField(
            model_name='questionentity',
            name='subsection',
            field=models.ForeignKey(help_text='The section this question belongs to.', on_delete=django.db.models.deletion.CASCADE, related_name='entities', to='questions.Subsection', verbose_name='Catalog'),
        ),
        migrations.AlterField(
            model_name='section',
            name='catalog',
            field=models.ForeignKey(help_text='The catalog this section belongs to.', on_delete=django.db.models.deletion.CASCADE, related_name='sections', to='questions.Catalog', verbose_name='Catalog'),
        ),
        migrations.AlterField(
            model_name='section',
            name='label_de',
            field=models.TextField(help_text='The German label for this section (auto-generated).', verbose_name='Label (de)'),
        ),
        migrations.AlterField(
            model_name='section',
            name='label_en',
            field=models.TextField(help_text='The English label for this section (auto-generated).', verbose_name='Label (en)'),
        ),
        migrations.AlterField(
            model_name='section',
            name='order',
            field=models.IntegerField(default=0, help_text='The position of this section in lists.', verbose_name='Order'),
        ),
        migrations.AlterField(
            model_name='section',
            name='title_de',
            field=models.CharField(help_text='The German title for this section.', max_length=256, verbose_name='Title (de)'),
        ),
        migrations.AlterField(
            model_name='section',
            name='title_en',
            field=models.CharField(help_text='The English title for this section.', max_length=256, verbose_name='Title (en)'),
        ),
        migrations.AlterField(
            model_name='subsection',
            name='label_de',
            field=models.TextField(help_text='The German label for this subsection (auto-generated).', verbose_name='Label (de)'),
        ),
        migrations.AlterField(
            model_name='subsection',
            name='label_en',
            field=models.TextField(help_text='The English label for this subsection (auto-generated).', verbose_name='Label (en)'),
        ),
        migrations.AlterField(
            model_name='subsection',
            name='order',
            field=models.IntegerField(default=0, help_text='The position of this subsection in lists.', verbose_name='Order'),
        ),
        migrations.AlterField(
            model_name='subsection',
            name='section',
            field=models.ForeignKey(help_text='The section this subsection belongs to.', on_delete=django.db.models.deletion.CASCADE, related_name='subsections', to='questions.Section', verbose_name='Catalog'),
        ),
        migrations.AlterField(
            model_name='subsection',
            name='title_de',
            field=models.CharField(help_text='The German title for this subsection.', max_length=256, verbose_name='Title (de)'),
        ),
        migrations.AlterField(
            model_name='subsection',
            name='title_en',
            field=models.CharField(help_text='The English title for this subsection.', max_length=256, verbose_name='Title (en)'),
        ),
    ]
