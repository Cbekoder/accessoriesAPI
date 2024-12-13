from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import InputListSerializer, InputListCreateSerializer, OutputCreateSerializer, OutputGetSerializer, \
    SaleItemGetSerializer, SaleItemPostSerializer, SalesListGetSerializer, SalesListPostSerializer
from .models import InputList, Output, SalesList


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



