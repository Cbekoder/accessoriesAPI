from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from .models import Product, Expense


class ProductTempSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'code', 'name', 'min_amount']
        read_only_fields = ['id']


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class ProductJustSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'code', 'name']

class ProductMinSerializer(ModelSerializer):
    status = SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'code', 'name', 'amount', 'min_amount', 'status']

    def get_status(self, obj):
        if obj.amount == obj.min_amount:
            return "Minimum"
        elif obj.amount < obj.min_amount and obj.amount > 0:
            return "Kam qolgan"
        elif obj.amount == 0:
            return "Tugagan"
        return "Yetarli"


class ExpenseListSerializer(ModelSerializer):
    class Meta:
        model = Expense
        fields = ['id', 'reason', 'description', 'total_sum', 'created_at']
        read_only_fields = ['id', 'created_at']

class ExpenseRetrieveSerializer(ModelSerializer):
    class Meta:
        model = Expense
        fields = ['id', 'reason', 'description', 'total_sum', 'created_at']
        read_only_fields = ['id', 'created_at', 'total_sum']