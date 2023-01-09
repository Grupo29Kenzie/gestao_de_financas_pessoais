from rest_framework import serializers
from .models import Saving

class SavingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Saving
        fields = [
            "id",
            "value"
        ]

        read_only_fields = ["id"]
