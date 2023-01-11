from rest_framework import serializers
from .models import User
from categories.models import Category
from savings.models import Saving
from savings.serializers import SavingSerializer
import ipdb


class UserSerializer(serializers.ModelSerializer):
    balance = serializers.SerializerMethodField()
    expenses = serializers.SerializerMethodField()
    entries = serializers.SerializerMethodField()
    cards = serializers.SerializerMethodField()

    def get_balance(self, obj: User):
        actual_balance = obj.balance
        expenses_entries = obj.expense_entrie.all()
        for item in expenses_entries:
            if item.is_paid:
                if item.transaction == "EXPENSE":
                    actual_balance -= item.value
                else:
                    actual_balance += item.value
        return actual_balance

    def get_expenses(self, obj: User):
        expenses_queryset = obj.expense_entrie.filter(transaction="EXPENSE").all()
        result = expenses_queryset.values()
        expenses = [
            {
                "name": entry["name"],
                "value": entry["value"],
                "expiration": entry["expiration"],
                "is_paid": entry["is_paid"],
                "category": Category.objects.filter(id=entry["category_id"])[0].name,
            }
            for entry in result
        ]
        return expenses

    def get_entries(self, obj: User):
        entries_queryset = obj.expense_entrie.filter(transaction="ENTRIE").all()
        result = entries_queryset.values()

        entries = [
            {
                "name": entry["name"],
                "value": entry["value"],
                "expiration": entry["expiration"],
                "is_paid": entry["is_paid"],
                "category": Category.objects.filter(id=entry["category_id"])[0].name,
            }
            for entry in result
        ]
        return entries

    def get_cards(self, obj: User):
        cards_queryset = obj.credit_cards.all().values()
        return cards_queryset

    # def create(self, validated_data: dict) -> User:
    #     if validated_data.get("admin", False):
    #         saving_data = validated_data.pop("saving")

    #         saving_obj, _ = Saving.objects.get_or_create(**saving_data)
    #         return User.objects.create_superuser(saving=saving_obj, **validated_data)
    #     saving_data = validated_data.pop("saving")
    #     saving_obj, _ = Saving.objects.get_or_create(**saving_data)
    #     return User.objects.create_user(saving=saving_obj, **validated_data)

    def update(self, instance: User, validated_data: dict) -> User:
        for key, value in validated_data.items():
            if key == "credit_cards":
                raise ValueError("Este campo deve ser atualizado da rota específica")
            if key == "expense_entrie":
                raise ValueError("Este campo deve ser atualizado da rota específica")
            if key == "password":
                instance.set_password(value)
            else:
                setattr(instance, key, value)
        instance.save()
        return instance

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "password",
            "cpf",
            "email",
            "expense_entrie",
            "entries",
            "expenses",
            "cards",
            "credit_cards",
            "saving",
            "balance",
        ]
        read_only_fields = ["saving", "expenses", "entries"]
        extra_kwargs = {
            "password": {"write_only": True},
            "expense_entrie": {"write_only": True},
            "credit_cards": {"write_only": True},
        }


class UserCreateSerializer(serializers.ModelSerializer):
    expenses = serializers.SerializerMethodField()
    entries = serializers.SerializerMethodField()
    cards = serializers.SerializerMethodField()
    saving = SavingSerializer()

    def get_expenses(self, obj: User):
        expenses_queryset = obj.expense_entrie.filter(transaction="EXPENSE").all()
        result = expenses_queryset.values()
        expenses = [
            {
                "name": entry["name"],
                "value": entry["value"],
                "expiration": entry["expiration"],
                "is_paid": entry["is_paid"],
                "category": Category.objects.filter(id=entry["category_id"])[0].name,
            }
            for entry in result
        ]
        return expenses

    def get_entries(self, obj: User):
        entries_queryset = obj.expense_entrie.filter(transaction="ENTRIE").all()
        result = entries_queryset.values()

        entries = [
            {
                "name": entry["name"],
                "value": entry["value"],
                "expiration": entry["expiration"],
                "is_paid": entry["is_paid"],
                "category": Category.objects.filter(id=entry["category_id"])[0].name,
            }
            for entry in result
        ]
        return entries

    def get_cards(self, obj: User):
        cards_queryset = obj.credit_cards.all().values()
        return cards_queryset

    def create(self, validated_data: dict) -> User:
        if validated_data.get("admin", False):
            saving_data = validated_data.pop("saving")
            saving_obj = Saving.objects.create(**saving_data)
            return User.objects.create_superuser(saving=saving_obj, **validated_data)
        saving_data = validated_data.pop("saving")
        saving_obj = Saving.objects.create(**saving_data)
        return User.objects.create_user(saving=saving_obj, **validated_data)

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "password",
            "cpf",
            "email",
            "entries",
            "expenses",
            "cards",
            "saving",
            "balance",
            "is_superuser",
            "admin",
        ]
        read_only_fields = [
            "expenses",
            "entries",
            "is_superuser",
        ]
        extra_kwargs = {"password": {"write_only": True}}
