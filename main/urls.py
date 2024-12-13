from django.urls import path
from .views import *


urlpatterns = [
    path('input/', InputListCreateAPIView.as_view(), name='input-list'),
    # path('template/<int:pk>/', ProductTempDetailView.as_view(), name='template-detail'),
    path('output/', OutputListCreateAPIView.as_view(), name='output-list'),
    # path('product-code/', ProductCodeView.as_view(), name='products-code'),
    path('sale/', SalesListCreate.as_view(), name='sale-list'),
    # path('expense/<int:pk>/', ExpenseDetailView.as_view(), name='expenses-detail'),
]