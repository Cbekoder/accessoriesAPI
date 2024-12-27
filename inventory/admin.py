from django.contrib import admin
from .models import Product, Expense


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'name', 'amount', 'arrival_price', 'sell_price', 'min_amount')
    list_display_links = ('id', 'code', 'name')
    search_fields = ('code', 'name')
    list_filter = ('amount', 'min_amount')
    ordering = ('-id',)


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('id', 'reason', 'total_sum', 'created_at')
    list_display_links = ('id', 'reason')
    search_fields = ('reason',)
    list_filter = ('created_at',)
    ordering = ('-created_at',)
