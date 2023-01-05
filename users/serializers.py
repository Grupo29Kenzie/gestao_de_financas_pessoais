from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    balance = serializers.SerializerMethodField()

    def get_balance(self, obj: User):
        actual_balance = 0
        return actual_balance

    def create(self, validated_data: dict) -> User:
        return User.objects.create_user(**validated_data)

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "password",
            "cpf",
            "email",
            "balance"
        ]

        read_only_fields = ["balance"]
        extra_kwargs = {'password': {'write_only': True}}
