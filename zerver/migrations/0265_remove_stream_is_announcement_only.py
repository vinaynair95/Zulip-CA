# Generated by Django 1.11.26 on 2020-01-27 22:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("zerver", "0264_migrate_is_announcement_only"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="stream",
            name="is_announcement_only",
        ),
    ]