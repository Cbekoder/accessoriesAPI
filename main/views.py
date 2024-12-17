from django.db.models import Sum
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from django.utils.timezone import now
from inventory.models import Product
from inventory.serializers import ProductJustSerializer
from datetime import datetime, timedelta
from .serializers import InputListSerializer, InputListCreateSerializer, OutputCreateSerializer, OutputGetSerializer, \
    SaleItemGetSerializer, SaleItemPostSerializer, SalesListGetSerializer, SalesListPostSerializer
from .models import InputList, Output, SalesList, SaleItem


class InputListCreateAPIView(ListCreateAPIView):
    queryset = InputList.objects.all()
    serializer_class = InputListSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return InputListSerializer
        return InputListCreateSerializer


class OutputListCreateAPIView(ListCreateAPIView):
    queryset = Output.objects.all()
    serializer_class = OutputCreateSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return OutputGetSerializer
        return OutputCreateSerializer



class SalesListCreateAPIView(ListCreateAPIView):
    queryset = SalesList.objects.all()
    serializer_class = SalesListGetSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return SalesListGetSerializer
        return SalesListPostSerializer



class TopSalesView(APIView):
    def get(self, request, *args, **kwargs):
        # Query parameters
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')

        try:
            if not end_date:
                end_date = now()
            else:
                end_date = datetime.strptime(end_date, '%Y-%m-%d')

            if not start_date:
                start_date = end_date - timedelta(days=30)
            else:
                start_date = datetime.strptime(start_date, '%Y-%m-%d')
        except ValueError:
            raise ValidationError("Invalid date format. Use YYYY-MM-DD.")

        sales_data = (
            SaleItem.objects.filter(sales_list__created_at__range=[start_date, end_date])
            .values('product')
            .annotate(total_amount=Sum('amount'))
            .order_by('-total_amount')
        )

        response_data = []
        for item in sales_data:
            product_id = item['product']
            try:
                product = Product.objects.get(id=product_id)
                product_data = ProductJustSerializer(product).data
            except Product.DoesNotExist:
                product_data = None

            response_data.append({
                "product": product_data,
                "total_sales": item['total_amount']
            })

        return Response(response_data)



