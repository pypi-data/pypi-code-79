# Generated by Django 3.0.7 on 2021-03-05 15:55

from django.db import migrations
import jutil.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ("jsanctions", "0004_auto_20200629_0350"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="eucombinedsanctionslist",
            name="global_file_id",
        ),
        migrations.AddField(
            model_name="sanctionslistfile",
            name="global_file_id",
            field=jutil.modelfields.SafeCharField(
                blank=True, default="", max_length=512, verbose_name="global file id"
            ),
        ),
    ]
