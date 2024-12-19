from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import InputList, InputListItem, Output, SaleItem, SalesList
from inventory.serializers import ProductSerializer, ProductJustSerializer


class InputListItemSerializer(serializers.ModelSerializer):
    product = ProductJustSerializer(read_only=True)
    class Meta:
        model = InputListItem
        fields = ['id', 'product', 'amount', 'arrival_price', 'sell_price', 'total_sum']
        read_only_fields = ['total_sum']

class InputListSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%d.%m.%Y %H:%M", read_only=True)
    products = InputListItemSerializer(many=True, source='inputlistitem_set')
    products_count = serializers.SerializerMethodField()

    class Meta:
        model = InputList
        fields = ['id', 'total', 'created_at', 'products_count', 'products']
        read_only_fields = ['total', 'created_at']

    def get_products_count(self, obj):
        return obj.inputlistitem_set.count()


class InputListItemCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = InputListItem
        fields = ['id', 'product', 'amount', 'arrival_price', 'sell_price', 'total_sum']
        read_only_fields = ['total_sum']

    def create(self, validated_data):
        input_list = validated_data.pop('input_list')
        instance = InputListItem.objects.create(input_list=input_list, **validated_data)
        return instance

class InputListCreateSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%d.%m.%Y %H:%M", read_only=True)
    products = InputListItemCreateSerializer(many=True, source='inputlistitem_set')

    class Meta:
        model = InputList
        fields = ['id', 'total', 'created_at', 'products']
        read_only_fields = ['total', 'created_at']

    def create(self, validated_data):
        items_data = validated_data.pop('inputlistitem_set')
        input_list = InputList.objects.create(total=0.0)
        for item_data in items_data:
            InputListItem.objects.create(input_list=input_list, **item_data)
        return input_list


class OutputCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Output
        fields = ['product', 'amount', 'reason']

class OutputGetSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%d.%m.%Y %H:%M")
    product = ProductSerializer()
    class Meta:
        model = Output
        fields = ['id', 'product', 'amount', 'reason', 'created_at']



class SaleItemPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleItem
        fields = ['id', 'product', 'amount', 'sell_price', 'total_sum']
        read_only_fields = ['id', 'total_sum',]

    def create(self, validated_data):
        return SaleItem.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance


class SalesListPostSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%d.%m.%Y %H:%M", read_only=True)
    products = SaleItemPostSerializer(many=True)

    class Meta:
        model = SalesList
        fields = ['id', 'created_at', 'total_sum', 'products']
        read_only_fields = ['id', 'created_at', 'total_sum']

    def create(self, validated_data):
        sale_items_data = validated_data.pop('products')

        sales_list = SalesList.objects.create(total_sum=0.0)
        sold_products = []
        for item_data in sale_items_data:
            instance = SaleItem.objects.create(sales_list=sales_list, **item_data)
            sold_products.append(instance)
        sales_list.products = sold_products
        return sales_list

    def validate_products(self, value):
        if not value or len(value) == 0:
            raise ValidationError({"error": "At least one product is required"})
        return value


class SaleItemGetSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = SaleItem
        fields = ['id', 'product', 'amount', 'sell_price', 'total_sum']


class SalesListGetSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%d.%m.%Y %H:%M")
    products = SaleItemGetSerializer(many=True, source='saleitem_set')
    products_count = serializers.SerializerMethodField()

    class Meta:
        model = SalesList
        fields = ['id', 'created_at', 'total_sum', 'products_count', 'products']

    def get_products_count(self, obj):
        return obj.saleitem_set.count()



