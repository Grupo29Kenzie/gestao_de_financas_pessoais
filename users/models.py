from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    cpf = models.CharField(max_length=11, unique=True)
    email = models.EmailField(max_length=30, unique=True)
    balance = models.IntegerField(null=True, default=0)
    saving = models.ForeignKey(
        "savings.Saving",
        on_delete=models.CASCADE,
        related_name="user",
        null=True
    )