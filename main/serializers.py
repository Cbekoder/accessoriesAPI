from rest_framework import serializers
from .models import InputList, InputListItem, Output, SaleItem, SalesList
from inventory.models import Product
from inventory.serializers import ProductSerializer



class InputListItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    class Meta:
        model = InputListItem
        fields = ['id', 'product', 'amount', 'total_sum']
        read_only_fields = ['total_sum']

class InputListSerializer(serializers.ModelSerializer):
    products = InputListItemSerializer(many=True, source='inputlistitem_set')

    class Meta:
        model = InputList
        fields = ['id', 'total', 'created_at', 'products']
        read_only_fields = ['total', 'created_at']



class InputListItemCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = InputListItem
        fields = ['id', 'product', 'amount', 'total_sum']
        read_only_fields = ['total_sum']

    def create(self, validated_data):
        input_list = validated_data.pop('input_list')
        instance = InputListItem.objects.create(input_list=input_list, **validated_data)
        return instance

class InputListCreateSerializer(serializers.ModelSerializer):
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
    product = ProductSerializer()
    class Meta:
        model = Output
        fields = ['id', 'product', 'amount', 'reason', 'created_at']



class SaleItemPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleItem
        fields = ['id', 'sales_list', 'product', 'amount', 'total_sum']
        read_only_fields = ['id', 'total_sum', 'sales_list']

    def create(self, validated_data):
        return SaleItem.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance


class SalesListPostSerializer(serializers.ModelSerializer):
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


class SaleItemGetSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = SaleItem
        fields = ['id', 'sales_list', 'product', 'amount', 'total_sum']


class SalesListGetSerializer(serializers.ModelSerializer):
    products = SaleItemPostSerializer(many=True, source='saleitem_set')

    class Meta:
        model = SalesList
        fields = ['id', 'created_at', 'total_sum', 'products']




