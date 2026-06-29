from rest_framework import serializers
from .models import Status, Type, Category, Subcategory, CashFlowRecord


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = "__all__"


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    type_name = serializers.CharField(source="type.name", read_only=True)

    class Meta:
        model = Category
        fields = ["id", "name", "type", "type_name"]


class SubcategorySerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source="category.name", read_only=True)

    class Meta:
        model = Subcategory
        fields = ["id", "name", "category", "category_name"]


class CashFlowRecordSerializer(serializers.ModelSerializer):
    status_name = serializers.CharField(source="status.name", read_only=True)
    type_name = serializers.CharField(source="type.name", read_only=True)
    category_name = serializers.CharField(source="category.name", read_only=True)
    subcategory_name = serializers.CharField(source="subcategory.name", read_only=True)

    class Meta:
        model = CashFlowRecord
        fields = [
            "id", "date",
            "status", "status_name",
            "type", "type_name",
            "category", "category_name",
            "subcategory", "subcategory_name",
            "amount", "comment",
            "created_at", "updated_at",
        ]

    def validate(self, data):
        category = data.get("category") or (self.instance and self.instance.category)
        subcategory = data.get("subcategory") or (self.instance and self.instance.subcategory)
        op_type = data.get("type") or (self.instance and self.instance.type)

        if category and op_type and category.type_id != op_type.id:
            raise serializers.ValidationError(
                {"category": "Категория не относится к выбранному типу."}
            )
        if subcategory and category and subcategory.category_id != category.id:
            raise serializers.ValidationError(
                {"subcategory": "Подкатегория не относится к выбранной категории."}
            )
        return data
