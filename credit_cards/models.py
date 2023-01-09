from django.db import models


class Credit_Card(models.Model):
    name = models.CharField(max_length=20)
    due_date = models.PositiveIntegerField()
    closing_day = models.PositiveIntegerField()
    limit = models.DecimalField(max_digits=12, decimal_places=2)
    is_paid = models.BooleanField(default=False)
    value = models.DecimalField(max_digits=12, decimal_places=2)
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="credit_cards",
    )
