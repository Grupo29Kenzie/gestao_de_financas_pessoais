from django.db import models


class TransactionOption(models.TextChoices):
    EXPENSE = "EXPENSE"
    ENTRIE = "ENTRIE"


class PaymentOption(models.TextChoices):
    MONEY = "MONEY"
    CREDIT_CARD = "CREDIT CARD"


class ExpenseEntrie(models.Model):
    transaction = models.CharField(
        max_length=15,
        choices=TransactionOption.choices,
    )
    payment = models.CharField(
        max_length=15, choices=PaymentOption.choices, default=PaymentOption.MONEY
    )
    name = models.CharField(max_length=127)
    expiration = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    value = models.FloatField()
    is_paid = models.BooleanField(default=False)
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="expense_entrie",
    )
    category = models.ForeignKey(
        "categories.Category",
        on_delete=models.CASCADE,
        related_name="expense_entrie",
        null=True
    )
