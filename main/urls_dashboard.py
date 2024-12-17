from django.urls import path
from .views import *


urlpatterns = [
    path('top-sales/', TopSalesView.as_view(), name='top-sales'),
]