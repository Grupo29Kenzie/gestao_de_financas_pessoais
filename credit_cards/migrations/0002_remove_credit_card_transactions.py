# Generated by Django 4.1.5 on 2023-01-09 14:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("credit_cards", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="credit_card",
            name="transactions",
        ),
    ]