from django.contrib import admin
from django.contrib.auth.models import Group
from .models import InputList, InputListItem, Output, SalesList, SaleItem

admin.site.unregister(Group)

class InputListItemInline(admin.TabularInline):
    model = InputListItem
    extra = 1
    fields = ('product', 'arrival_price', 'sell_price', 'amount', 'total_sum')
    readonly_fields = ('total_sum',)


@admin.register(InputList)
class InputListAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'total')
    list_display_links = ('id', 'created_at')
    inlines = [InputListItemInline]
    readonly_fields = ('total',)
    ordering = ('-created_at',)


@admin.register(Output)
class OutputAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'created_at', 'amount', 'reason')
    list_display_links = ('id', 'product')
    search_fields = ('product__name', 'reason')
    list_filter = ('created_at',)
    ordering = ('-created_at',)


class SaleItemInline(admin.TabularInline):
    model = SaleItem
    extra = 1
    fields = ('product', 'amount', 'sell_price', 'total_sum')
    readonly_fields = ('total_sum',)


@admin.register(SalesList)
class SalesListAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'total_sum')
    list_display_links = ('id', 'created_at')
    inlines = [SaleItemInline]
    readonly_fields = ('total_sum',)
    ordering = ('-created_at',)
