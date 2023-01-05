from rest_framework import serializers
from .models import ExpenseEntrie


class ExpenseEntrieSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return ExpenseEntrie.objects.create(**validated_data)

    class Meta:
        model = ExpenseEntrie
        fields = [
            "id",
            "name",
            "created_at",
            "expiration",
            "value",
            "transaction",
            "payment",
            "is_paid",
            "user_id",
        ]

        read_only_fields = ["id", "created_at"]
