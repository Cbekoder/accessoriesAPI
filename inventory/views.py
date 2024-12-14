from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import F
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .models import Product, Expense
from .serializers import ProductTempSerializer, ExpenseListSerializer, ExpenseRetrieveSerializer, ProductSerializer


class ProductTempListView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductTempSerializer

class ProductTempDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductTempSerializer

class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'min',
                openapi.IN_QUERY,
                description="Filter products where amount <= min_amount (true/false)",
                type=openapi.TYPE_BOOLEAN,
                required=False,
            ),
        ]
    )
    def get(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def get_queryset(self):

        minimum = self.request.query_params.get('min')
        if minimum and minimum.lower() in ['yes', 'true']:
            self.queryset = self.queryset.filter(amount__lte=F("min_amount"))
        else:
            self.queryset = self.queryset.filter(amount__gt=0)

        self.queryset = self.queryset.order_by('name', '-amount')

        return self.queryset


class ProductCodeView(APIView):
    @swagger_auto_schema(
        operation_summary="Retrieve product details",
        operation_description="Get product details based on the code provided in the request header.",
        manual_parameters=[
            openapi.Parameter(
                'code',
                openapi.IN_HEADER,
                description="The unique code of the product to retrieve.",
                type=openapi.TYPE_STRING,
                required=True,
            )
        ],
        responses={
            200: ProductSerializer(),
            400: openapi.Response(description="Code header is required."),
            404: openapi.Response(description="Product with the given code does not exist."),
        },
    )
    def get(self, request):
        code = request.headers.get('Code')
        if not code:
            return Response({"error": "Code header is required."}, status=status.HTTP_400_BAD_REQUEST)
        try:
            product = Product.objects.get(code=code)
            serializer = ProductSerializer(product)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            return Response({"error": "Product with the given code does not exist."}, status=status.HTTP_404_NOT_FOUND)


class ExpensesListCreateView(ListCreateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseListSerializer

class ExpenseDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseRetrieveSerializer