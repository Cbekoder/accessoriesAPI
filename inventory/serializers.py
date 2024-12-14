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