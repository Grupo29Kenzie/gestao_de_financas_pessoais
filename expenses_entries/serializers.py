from rest_framework import serializers
from .models import ExpenseEntrie, TransactionOption, PaymentOption
from categories.serializers import CategorySerializer
from categories.models import Category


class ExpenseEntrieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    created_at = serializers.DateTimeField(read_only=True)
    expiration = serializers.DateField()
    value = serializers.FloatField()
    transaction = serializers.ChoiceField(
        choices=TransactionOption.choices
    )
    payment = serializers.ChoiceField(
        choices=PaymentOption.choices, default=PaymentOption.MONEY
    )
    is_paid = serializers.BooleanField(default=False)
    user_id = serializers.IntegerField(read_only=True)
    category = CategorySerializer()


    def create(self, validated_data):
        category_data = validated_data.pop("category")
        category_obj, _ = Category.objects.get_or_create(**category_data)
        expense_entrie = ExpenseEntrie.objects.create(category=category_obj, **validated_data)
        return expense_entrie
    