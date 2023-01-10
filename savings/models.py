from django.db import models
from users.models import User

class Saving(models.Model):
    value = models.FloatField()

    # user_id = models.OneToOneField(
    #    User,
    #    on_delete=models.CASCADE,
    #    related_name="user_id",
    # )

