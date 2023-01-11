from rest_framework import serializers
from .models import Saving
from users.models import User


class SavingSerializer(serializers.ModelSerializer):
    owner_id = serializers.SerializerMethodField(read_only=True)

    def get_owner_id(self, obj: User):
        return obj.id

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        return instance

    class Meta:
        model = Saving
        fields = ["id", "value", "owner_id"]

        # read_only_fields = ["user_id"]
