from django.db import models
from users.models import User

class Saving(models.Model):
    value = models.FloatField()


