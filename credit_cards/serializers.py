from rest_framework import serializers
from .models import Credit_Card


class CreditCardSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Credit_Card.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        return instance

    class Meta:
        model = Credit_Card
        fields = [
            "id",
            "name",
            "due_date",
            "closing_day",
            "limit",
            "is_paid",
            "value",
        ]

    read_only_fields = ["id"]
