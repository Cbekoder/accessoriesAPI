from django.urls import path
from .views import *


urlpatterns = [
    path('templates/', ProductTempListView.as_view(), name='template-list'),
    path('template/<int:pk>/', ProductTempDetailView.as_view(), name='template-detail'),
    path('products/', ProductListView.as_view(), name='products-list'),
    path('product/<int:pk>', ProductRetrieveAPIView.as_view(), name='products-detail'),
    path('product-code/', ProductCodeView.as_view(), name='products-code'),
    path('expenses/', ExpensesListCreateView.as_view(), name='expenses-list'),
    path('expense/<int:pk>/', ExpenseDetailView.as_view(), name='expenses-detail'),
]