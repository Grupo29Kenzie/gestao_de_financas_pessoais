from django.db import models
from expenses_entries.models import TransactionOption


class Credit_Card(models.Model):
    name = models.CharField(max_length=20)
    due_date = models.PositiveIntegerField()
    closing_day = models.PositiveBigIntegerField()
    limit = models.DecimalField(max_digits=12, decimal_places=2)
    transactions = models.CharField(
        max_length=15,
        choices=TransactionOption.choices,
        default=TransactionOption.EXPENSE,
    )
    is_paid = models.BooleanField(default=False)
    value = models.DecimalField(max_digits=12, decimal_places=2)
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="credit_cards",
    )
