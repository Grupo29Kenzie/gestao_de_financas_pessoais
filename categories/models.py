from django.db import models


class Category(models.Model):
    class Meta:
        ordering = ["id"]

    name: models.CharField(max_length=200)
