# Generated by Django 1.11.5 on 2017-10-28 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("zerver", "0115_user_groups"),
    ]

    operations = [
        migrations.AddField(
            model_name="realm",
            name="allow_message_deleting",
            field=models.BooleanField(default=False),
        ),
    ]
