from django.db import models


class Product(models.Model):
    code = models.CharField(max_length=100, unique=True, null=True, blank=True)
    name = models.CharField(max_length=255)
    amount = models.PositiveIntegerField(default=0)
    arrival_price = models.FloatField(null=True, blank=True)
    sell_price = models.FloatField(null=True, blank=True)
    min_amount = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Mahsulot '
        verbose_name_plural = 'Mahsulotlar '
        ordering = ['-id']



class Expense(models.Model):
    reason = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    total_sum = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.reason

    class Meta:
        verbose_name = 'Xarajat '
        verbose_name_plural = 'Xarajatlar '
        ordering = ['-created_at']
