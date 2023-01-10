from rest_framework import serializers
from .models import Saving
from users.models import User


class SavingSerializer(serializers.ModelSerializer):
    user_id = serializers.SerializerMethodField()

    def get_user_id(self, obj: User):
        return obj.user.id
        

    class Meta:
        model = Saving
        fields = [
            "id",
            "value",
            "user_id"
        ]

        read_only_fields = ['user_id']