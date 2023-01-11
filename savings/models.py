from django.db import models
from users.models import User


class Saving(models.Model):
    value = models.FloatField()
    user = models.OneToOneField(
        "users.User",
        on_delete=models.CASCADE,
        related_name="saving",
        null=True,
    )
