# Generated by Django 4.1.5 on 2023-01-06 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Credit_Card",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("due_date", models.PositiveIntegerField()),
                ("closing_day", models.PositiveBigIntegerField()),
                ("limit", models.DecimalField(decimal_places=2, max_digits=12)),
                (
                    "transactions",
                    models.CharField(
                        choices=[("EXPENSE", "Expense"), ("ENTRIE", "Entrie")],
                        default="EXPENSE",
                        max_length=15,
                    ),
                ),
                ("is_paid", models.BooleanField(default=False)),
                ("value", models.DecimalField(decimal_places=2, max_digits=12)),
            ],
        ),
    ]
