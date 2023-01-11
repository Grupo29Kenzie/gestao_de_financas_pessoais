# Generated by Django 4.1.5 on 2023-01-11 15:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("savings", "0001_initial"),
        ("users", "0008_alter_user_admin"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="saving",
            field=models.OneToOneField(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="user",
                to="savings.saving",
            ),
            preserve_default=False,
        ),
    ]
