# Generated by Django 3.2.2 on 2021-05-15 18:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("zerver", "0338_migrate_to_add_custom_emoji_policy"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="realm",
            name="add_emoji_by_admins_only",
        ),
    ]
