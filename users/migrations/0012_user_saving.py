# Generated by Django 4.1.5 on 2023-01-11 19:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("savings", "0005_remove_saving_user"),
        ("users", "0011_remove_user_saving"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="saving",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="user",
                to="savings.saving",
            ),
        ),
    ]
