# Generated by Django 4.1.5 on 2023-01-09 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_alter_user_balance"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="admin",
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]